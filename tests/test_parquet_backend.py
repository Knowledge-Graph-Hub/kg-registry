"""Test Parquet backend functionality."""

from kg_registry.parquet_backend import DuckDBParquetQuerier, ParquetBackend, sync_yaml_to_parquet


def test_in_memory_backend():
    """Test in-memory Parquet backend."""
    backend = ParquetBackend()
    try:
        tables = backend.conn.execute("SHOW TABLES").fetchall()
        table_names = [table[0] for table in tables]

        assert "resources" in table_names
        assert "resource_domains" in table_names
        assert "resource_products" in table_names
        assert "resource_taxa" in table_names
    finally:
        backend.close()


def test_yaml_sync(parquet_backend_sample_data, parquet_yaml_writer, tmp_path):
    """Test syncing YAML data to Parquet."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)
    backend = ParquetBackend(str(tmp_path))

    try:
        count = backend.sync_from_yaml(str(yaml_file))
        assert count == 2

        parquet_files = [path.name for path in tmp_path.glob("*.parquet")]
        assert len(parquet_files) == 4

        resources = backend.conn.execute("SELECT * FROM resources").fetchall()
        assert len(resources) == 2

        domains = backend.conn.execute("SELECT * FROM resource_domains").fetchall()
        assert len(domains) == 3

        products = backend.conn.execute("SELECT * FROM resource_products").fetchall()
        assert len(products) == 1
    finally:
        backend.close()


def test_query_resources(parquet_backend_sample_data, parquet_yaml_writer):
    """Test querying resources with filters."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)
    backend = ParquetBackend()

    try:
        backend.sync_from_yaml(str(yaml_file))

        results = backend.query_resources(category="TestCategory")
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"

        results = backend.query_resources(activity_status="active")
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"

        results = backend.query_resources(domain="example")
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"
    finally:
        backend.close()


def test_search_resources(parquet_backend_sample_data, parquet_yaml_writer):
    """Test searching resources."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)
    backend = ParquetBackend()

    try:
        backend.sync_from_yaml(str(yaml_file))

        results = backend.search_resources("Test Resource 1")
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"

        results = backend.search_resources("Parquet testing")
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"

        results = backend.search_resources("nonexistent")
        assert len(results) == 0
    finally:
        backend.close()


def test_get_resource_stats(parquet_backend_sample_data, parquet_yaml_writer):
    """Test getting resource statistics."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)
    backend = ParquetBackend()

    try:
        backend.sync_from_yaml(str(yaml_file))
        stats = backend.get_resource_stats()

        assert stats["total_resources"] == 2
        assert stats["active_resources"] == 1
        assert stats["by_category"]["TestCategory"] == 1
        assert stats["by_category"]["AnotherCategory"] == 1
        assert stats["by_domain"]["test"] == 2
        assert stats["by_domain"]["example"] == 1
    finally:
        backend.close()


def test_sync_function(parquet_backend_sample_data, parquet_yaml_writer, tmp_path):
    """Test standalone sync function."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)
    count = sync_yaml_to_parquet(str(yaml_file), str(tmp_path))
    assert count == 2

    parquet_files = [path.name for path in tmp_path.glob("*.parquet")]
    assert len(parquet_files) == 4

    backend = ParquetBackend()
    try:
        backend.load_from_parquet(str(tmp_path))
        resources_count_row = backend.conn.execute("SELECT COUNT(*) FROM resources").fetchone()
        resources_count = resources_count_row[0] if resources_count_row else 0
        assert resources_count == 2
    finally:
        backend.close()


def test_duckdb_parquet_querier(parquet_backend_sample_data, parquet_yaml_writer, tmp_path):
    """Test DuckDBParquetQuerier."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)
    sync_yaml_to_parquet(str(yaml_file), str(tmp_path))

    with DuckDBParquetQuerier(str(tmp_path)) as querier:
        results = querier.execute_query("SELECT * FROM resources")
        assert len(results) == 2

        results = querier.execute_query(
            "SELECT * FROM resources WHERE category = ?",
            ["TestCategory"],
        )
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"

        results = querier.execute_query(
            """
            SELECT r.id, r.name, d.domain
            FROM resources r
            JOIN resource_domains d ON r.id = d.resource_id
            WHERE d.domain = 'example'
            """
        )
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"
        assert results[0]["domain"] == "example"


def test_context_manager(parquet_backend_sample_data, parquet_yaml_writer):
    """Test Parquet backend as context manager."""
    yaml_file = parquet_yaml_writer(parquet_backend_sample_data)

    with ParquetBackend() as backend:
        count = backend.sync_from_yaml(str(yaml_file))
        assert count == 2

        results = backend.query_active_resources()
        assert len(results) == 1


def test_taxon_insertion(parquet_backend_taxa_data, parquet_yaml_writer):
    """Test that taxa are inserted into the database."""
    yaml_file = parquet_yaml_writer(parquet_backend_taxa_data)
    backend = ParquetBackend()

    try:
        count = backend.sync_from_yaml(str(yaml_file))
        assert count == 2

        taxa = backend.conn.execute("SELECT * FROM resource_taxa").fetchall()
        assert len(taxa) == 3

        taxa_for_resource1 = backend.conn.execute(
            "SELECT taxon FROM resource_taxa WHERE resource_id = 'test-resource-1' ORDER BY taxon"
        ).fetchall()
        taxa_ids = [taxon[0] for taxon in taxa_for_resource1]
        assert "NCBITaxon:9606" in taxa_ids
        assert "NCBITaxon:10116" in taxa_ids
    finally:
        backend.close()


def test_query_by_taxon(parquet_backend_taxon_query_data, parquet_yaml_writer):
    """Test querying resources by taxon."""
    yaml_file = parquet_yaml_writer(parquet_backend_taxon_query_data)
    backend = ParquetBackend()

    try:
        backend.sync_from_yaml(str(yaml_file))

        results = backend.query_by_taxon("NCBITaxon:9606", include_descendants=False)
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-1"

        results = backend.query_by_taxon("NCBITaxon:10116", include_descendants=False)
        assert len(results) == 1
        assert results[0]["id"] == "test-resource-2"

        results = backend.query_by_taxon("NCBITaxon:999999", include_descendants=False)
        assert len(results) == 0
    finally:
        backend.close()


def test_taxon_table_in_sync(parquet_backend_single_taxon_data, parquet_yaml_writer, tmp_path):
    """Test that resource_taxa table is included when syncing to Parquet."""
    yaml_file = parquet_yaml_writer(parquet_backend_single_taxon_data)
    backend = ParquetBackend(str(tmp_path))

    try:
        count = backend.sync_from_yaml(str(yaml_file))
        assert count == 1

        parquet_files = [path.name for path in tmp_path.glob("*.parquet")]
        assert "resource_taxa.parquet" in parquet_files
        assert len(parquet_files) == 4

        backend2 = ParquetBackend()
        try:
            backend2.load_from_parquet(str(tmp_path))
            taxa_count_row = backend2.conn.execute("SELECT COUNT(*) FROM resource_taxa").fetchone()
            taxa_count = taxa_count_row[0] if taxa_count_row else 0
            assert taxa_count == 1
        finally:
            backend2.close()
    finally:
        backend.close()
