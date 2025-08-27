import importlib.util
import sys
from pathlib import Path

import duckdb  # type: ignore

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INGEST_PATH = ROOT / "src" / "kg_registry" / "ingests" / "kg-monarch" / "kg-monarch.py"


def _load_ingest_module():
    spec = importlib.util.spec_from_file_location("kg_monarch_ingest", str(INGEST_PATH))
    assert spec and spec.loader, "Failed to load ingest module spec"
    mod = importlib.util.module_from_spec(spec)
    sys.modules["kg_monarch_ingest"] = mod
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def _write_parquet_edges(path: Path):
    con = duckdb.connect(":memory:")
    # Minimal schema similar to QC edge report
    con.execute(
        """
        CREATE TABLE edges AS
        SELECT * FROM (
            VALUES
              ('biolink:Gene','biolink:interacts_with','biolink:Gene','prov_a','infores:a', 10),
              ('biolink:Gene','biolink:related_to','biolink:Gene','prov_b','infores:b', 5)
        ) AS t(subject_category, predicate, object_category, provided_by, primary_knowledge_source, count);
        """
    )
    con.execute(f"COPY edges TO '{path.as_posix()}' (FORMAT 'parquet')")
    con.close()


def _write_parquet_nodes(path: Path):
    con = duckdb.connect(":memory:")
    # Minimal schema similar to QC node report
    con.execute(
        """
        CREATE TABLE nodes AS
        SELECT * FROM (
            VALUES
              ('biolink:Gene', 'NCBITaxon:9606', 8, 8.0),
              ('biolink:Disease', 'NCBITaxon:9606', 2, 2.0)
        ) AS t(category, in_taxon, count, count_1);
        """
    )
    con.execute(f"COPY nodes TO '{path.as_posix()}' (FORMAT 'parquet')")
    con.close()


def test_counts_and_types_from_parquet(tmp_path):
    edge_pq = tmp_path / "edge_report.parquet"
    node_pq = tmp_path / "node_report.parquet"
    _write_parquet_edges(edge_pq)
    _write_parquet_nodes(node_pq)

    ingest = _load_ingest_module()

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
