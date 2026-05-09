"""Regression tests for graph visualization export helpers."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest


def _run_graph_export_harness() -> dict:
    """Execute the graph export helpers in Node with mocked browser primitives."""
    if shutil.which("node") is None:
        pytest.skip("node is required to execute the graph visualization export test")

    repo_root = Path(__file__).resolve().parents[1]
    source = (repo_root / "assets/js/kg-registry-kg-visualization-incremental.js").read_text()

    script = f"""
(async () => {{
const alerts = [];
let removedIcons = 0;
const downloads = [];
const blobStore = {{}};
const revokedUrls = [];
let blobCounter = 0;
let lastCanvasBlobType = null;
const NativeDate = Date;

function makeClone() {{
  return {{
    attrs: {{}},
    firstChild: null,
    setAttribute(name, value) {{
      this.attrs[name] = value;
    }},
    querySelectorAll(selector) {{
      if (selector !== 'foreignObject.node-icon') {{
        return [];
      }}
      return [
        {{ remove() {{ removedIcons += 1; }} }},
        {{ remove() {{ removedIcons += 1; }} }},
      ];
    }},
    insertBefore(node, before) {{
      this.firstChild = node;
    }},
  }};
}}

function createBlobContent(parts) {{
  return parts.map((part) => {{
    if (typeof part === 'string') {{
      return part;
    }}
    if (part && typeof part.content === 'string') {{
      return part.content;
    }}
    return '';
  }}).join('');
}}

const svgElement = {{
  querySelector(selector) {{
    if (selector === 'g.graph-elements') {{
      return {{
        getBBox() {{
          return {{ x: 10, y: 20, width: 300, height: 200 }};
        }},
      }};
    }}
    throw new Error(`Unexpected querySelector: ${{selector}}`);
  }},
  cloneNode() {{
    return makeClone();
  }},
}};

globalThis.document = {{
  addEventListener() {{}},
  querySelector(selector) {{
    if (selector === '#graph-container svg') {{
      return svgElement;
    }}
    throw new Error(`Unexpected document.querySelector: ${{selector}}`);
  }},
  createElement(tag) {{
    if (tag === 'canvas') {{
      return {{
        width: 0,
        height: 0,
        getContext() {{
          return {{
            drawImage() {{}},
          }};
        }},
        toBlob(callback, type) {{
          lastCanvasBlobType = type;
          callback({{ type }});
        }},
      }};
    }}
    if (tag === 'a') {{
      return {{
        href: null,
        download: null,
        click() {{
          downloads.push({{
            href: this.href,
            download: this.download,
            blobType: blobStore[this.href] ? blobStore[this.href].type : null,
            content: blobStore[this.href] ? blobStore[this.href].content : null,
          }});
        }},
      }};
    }}
    return {{}};
  }},
  createElementNS(ns, tag) {{
    return {{
      namespaceURI: ns,
      tagName: tag,
      attrs: {{}},
      setAttribute(name, value) {{
        this.attrs[name] = value;
      }},
    }};
  }},
}};

globalThis.alert = (message) => alerts.push(message);
globalThis.fetch = async () => ({{
  async json() {{
    return {{
      '@context': {{
        '@vocab': 'http://example.org/kg-registry/',
      }},
    }};
  }},
}});
globalThis.jsyaml = {{
  load() {{
    return {{ resources: [] }};
  }},
  dump(value) {{
    return JSON.stringify(value, null, 2);
  }},
}};
globalThis.d3 = {{}};
globalThis.Blob = class Blob {{
  constructor(parts, options = {{}}) {{
    this.parts = parts;
    this.type = options.type || null;
    this.content = createBlobContent(parts);
  }}
}};
globalThis.URL = {{
  createObjectURL(obj) {{
    const url = `blob:${{obj && obj.type ? obj.type : 'unknown'}}:${{blobCounter++}}`;
    blobStore[url] = {{
      type: obj && obj.type ? obj.type : null,
      content: obj && typeof obj.content === 'string' ? obj.content : '',
    }};
    return url;
  }},
  revokeObjectURL(url) {{
    revokedUrls.push(url);
  }},
}};
globalThis.XMLSerializer = class XMLSerializer {{
  serializeToString(node) {{
    return `<svg xmlns="${{node.attrs.xmlns}}" width="${{node.attrs.width}}" height="${{node.attrs.height}}"></svg>`;
  }}
}};
globalThis.Image = class Image {{
  set src(value) {{
    this._src = value;
    if (this.onload) {{
      this.onload();
    }}
  }}
}};
globalThis.Date = class extends Date {{
  constructor(...args) {{
    if (args.length === 0) {{
      super('2026-04-07T12:00:00Z');
    }} else {{
      super(...args);
    }}
  }}
  static now() {{
    return new NativeDate('2026-04-07T12:00:00Z').getTime();
  }}
}};

{source}

allResourceMap = {{
  res1: {{
    id: 'res1',
    name: 'Resource One',
    category: 'KnowledgeGraph',
    description: 'First resource',
    products: [{{ id: 'res1.graph', category: 'GraphProduct' }}],
  }},
  res2: {{
    id: 'res2',
    name: 'Resource Two',
    category: 'DataSource',
    description: 'Second resource',
  }},
}};
activeResourceIds = new Set(['res1']);
displayedGraph = {{
  nodes: [
    {{ id: 'res1', name: 'Resource One', type: 'KnowledgeGraph' }},
    {{ id: 'res1.graph', name: 'Primary Graph', type: 'GraphProduct', parentId: 'res1' }},
    {{ id: 'res2', name: 'Resource Two', type: 'DataSource' }},
  ],
  links: [
    {{ source: 'res1', target: 'res1.graph', type: 'has_product' }},
    {{ source: 'res1.graph', target: 'res1', type: 'derived_from', relationType: 'prov:hadPrimarySource' }},
    {{ source: 'res1.graph', target: 'res2', type: 'derived_from', relationType: 'prov:wasInfluencedBy' }},
    {{ source: 'res1.graph', target: 'res2', type: 'derived_from', relationType: 'prov:hadPrimarySource' }},
  ],
}};

exportAsSVG();
exportAsPNG();
exportAsTSV();
await exportAsYAML();
await exportAsJSONLD();

console.log(JSON.stringify({{
  alerts,
  removedIcons,
  downloads,
  revokedUrls,
  lastCanvasBlobType,
}}));
}})().catch((error) => {{
  console.error(error);
  process.exit(1);
}});
"""

    result = subprocess.run(
        ["node", "-"],
        input=script,
        text=True,
        capture_output=True,
        check=True,
        cwd=repo_root,
    )

    return json.loads(result.stdout.strip())


def test_graph_export_options_work() -> None:
    """Ensure all graph export options produce downloads with expected payloads."""
    payload = _run_graph_export_harness()

    assert payload["alerts"] == []
    assert payload["removedIcons"] == 2
    assert payload["lastCanvasBlobType"] == "image/png"

    downloads = {item["download"]: item for item in payload["downloads"]}

    svg = downloads["kg-registry-graph-2026-04-07.svg"]
    assert svg["blobType"] == "image/svg+xml"
    assert "<svg" in svg["content"]
    assert 'xmlns="http://www.w3.org/2000/svg"' in svg["content"]

    png = downloads["kg-registry-graph-2026-04-07.png"]
    assert png["blobType"] == "image/png"
    assert png["href"].startswith("blob:image/png")

    tsv = downloads["kg-registry-interactions-2026-04-07.tsv"]
    assert tsv["blobType"] == "text/tab-separated-values"
    assert "source\ttarget\trelationship_type" in tsv["content"]
    assert "res1.graph\tres1\tprov:hadPrimarySource" in tsv["content"]
    assert "res1.graph\tres2\tprov:hadPrimarySource" in tsv["content"]
    assert "res1\tres1.graph\thas_product" not in tsv["content"]
    assert "res1.graph\tres2\tprov:wasInfluencedBy" not in tsv["content"]

    yaml_export = downloads["kg-registry-data-2026-04-07.yml"]
    assert yaml_export["blobType"] == "text/yaml"
    assert '"resources": [' in yaml_export["content"]
    assert '"id": "res1"' in yaml_export["content"]
    assert '"id": "res2"' not in yaml_export["content"]

    jsonld_export = downloads["kg-registry-data-2026-04-07.jsonld"]
    assert jsonld_export["blobType"] == "application/ld+json"
    jsonld_payload = json.loads(jsonld_export["content"])
    assert jsonld_payload["@context"]["@vocab"] == "http://example.org/kg-registry/"
    assert len(jsonld_payload["@graph"]) == 1
    assert jsonld_payload["@graph"][0]["id"] == "res1"
    assert jsonld_payload["@graph"][0]["@id"] == "res1"

    assert len(payload["revokedUrls"]) == 6
