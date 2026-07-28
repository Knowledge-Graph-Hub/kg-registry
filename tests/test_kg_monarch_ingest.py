"""Test KG-Monarch ingest helpers against small parquet fixtures."""

from pathlib import Path

import duckdb  # type: ignore
import frontmatter


def _write_parquet_edges(path: Path):
    con = duckdb.connect(":memory:")
    # Minimal schema similar to QC edge report
    con.execute("""
        CREATE TABLE edges AS
        SELECT * FROM (
            VALUES
              ('biolink:Gene','biolink:interacts_with','biolink:Gene','prov_a','infores:a', 10),
              ('biolink:Gene','biolink:related_to','biolink:Gene','prov_b','infores:b', 5)
        ) AS t(subject_category, predicate, object_category, provided_by, primary_knowledge_source, count);
        """)
    con.execute(f"COPY edges TO '{path.as_posix()}' (FORMAT 'parquet')")
    con.close()


def _write_parquet_nodes(path: Path):
    con = duckdb.connect(":memory:")
    # Minimal schema similar to QC node report
    con.execute("""
        CREATE TABLE nodes AS
        SELECT * FROM (
            VALUES
              ('biolink:Gene', 'NCBITaxon:9606', 8, 8.0),
              ('biolink:Disease', 'NCBITaxon:9606', 2, 2.0)
        ) AS t(category, in_taxon, count, count_1);
        """)
    con.execute(f"COPY nodes TO '{path.as_posix()}' (FORMAT 'parquet')")
    con.close()


def test_counts_and_types_from_parquet(tmp_path, kg_monarch_ingest_module):
    edge_pq = tmp_path / "edge_report.parquet"
    node_pq = tmp_path / "node_report.parquet"
    _write_parquet_edges(edge_pq)
    _write_parquet_nodes(node_pq)

    ingest = kg_monarch_ingest_module

    # counts: edges=sum(count)=15, nodes=sum(count)=10 per our fixture
    ecount, ncount = ingest.counts_from_parquet(str(edge_pq), str(node_pq))
    assert ecount == 15
    assert ncount == 10

    # types
    preds, cats = ingest.types_from_parquet(str(edge_pq), str(node_pq))
    assert sorted(preds) == [
        "biolink:interacts_with",
        "biolink:related_to",
    ]
    assert sorted(cats) == [
        "biolink:Disease",
        "biolink:Gene",
    ]


RESOURCE_PAGE = """---
activity_status: active
category: KnowledgeGraph
id: kg-monarch
last_modified_date: '2020-01-01T00:00:00Z'
layout: resource_detail
name: Monarch Knowledge Graph
products:
- category: GraphProduct
  description: KGX distribution
  id: kg-monarch.graph
  name: KG-Monarch
- category: GraphProduct
  description: Propagated here because EpiGraphDB cites kg-monarch as a source
  id: epigraphdb.graph
  name: EpiGraphDB Graph
- category: GraphicalInterface
  description: Not a graph product
  id: kg-monarch.web
  name: Monarch Web
---

# Monarch Knowledge Graph

Curated body text.
"""


def _prepare_resource(tmp_path, ingest, monkeypatch):
    resource_file = tmp_path / "kg-monarch.md"
    resource_file.write_text(RESOURCE_PAGE, encoding="utf-8")
    monkeypatch.setattr(ingest, "RESOURCE_FILE", resource_file)
    return resource_file


def test_update_resource_writes_without_type_error(tmp_path, kg_monarch_ingest_module, monkeypatch):
    """The write-back path must not hand a str to a binary file handle."""
    ingest = kg_monarch_ingest_module
    resource_file = _prepare_resource(tmp_path, ingest, monkeypatch)

    changed = ingest.update_resource(
        edge_count=15_807_241,
        node_count=1_582_279,
        predicates=["biolink:interacts_with"],
        node_categories=["biolink:Gene"],
    )

    assert changed is True
    post = frontmatter.load(resource_file)
    assert "Curated body text." in post.content
    assert post.metadata["last_modified_date"] != "2020-01-01T00:00:00Z"


def test_update_resource_only_touches_products_it_owns(
    tmp_path, kg_monarch_ingest_module, monkeypatch
):
    """Products propagated onto the page belong to other resources.

    epigraphdb.graph is listed here only because EpiGraphDB cites kg-monarch as a
    source. Writing Monarch's counts and predicate lists onto it would describe
    EpiGraphDB's graph with Monarch's numbers.
    """
    ingest = kg_monarch_ingest_module
    resource_file = _prepare_resource(tmp_path, ingest, monkeypatch)

    ingest.update_resource(
        edge_count=15_807_241,
        node_count=1_582_279,
        predicates=["biolink:interacts_with"],
        node_categories=["biolink:Gene"],
    )

    products = {p["id"]: p for p in frontmatter.load(resource_file).metadata["products"]}

    assert products["kg-monarch.graph"]["edge_count"] == 15_807_241
    assert products["kg-monarch.graph"]["node_count"] == 1_582_279
    assert products["kg-monarch.graph"]["predicates"] == ["biolink:interacts_with"]

    for field in ("edge_count", "node_count", "predicates", "node_categories"):
        assert field not in products["epigraphdb.graph"], f"{field} written to a foreign product"
        assert field not in products["kg-monarch.web"], f"{field} written to a non-GraphProduct"


def test_owned_by_resource_rejects_string_prefix_matches(kg_monarch_ingest_module):
    ingest = kg_monarch_ingest_module

    assert ingest._owned_by_resource("kg-monarch.graph.neo4j")
    assert not ingest._owned_by_resource("kg-monarch-extras.graph")
    assert not ingest._owned_by_resource("epigraphdb.graph")
    assert not ingest._owned_by_resource("kg-monarch")
    assert not ingest._owned_by_resource(None)
