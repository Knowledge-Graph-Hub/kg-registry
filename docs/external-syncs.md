# External Syncs

KG-Registry includes a small set of scripted metadata syncs that pull structured data from external registries or release feeds and update curated resource pages in this repository.

## Current Sync Processes

| Sync | Script | Make target | KG-Registry scope | Upstream source |
| --- | --- | --- | --- | --- |
| FRINK OKN registry | `util/sync_frink.py` | `make sync-frink` | Creates or updates OKN resource pages and FRINK endpoint products | `https://raw.githubusercontent.com/frink-okn/okn-registry/main/docs/registry/kgs.yaml` |
| OBO Foundry registry | `util/sync_obo_foundry.py` | `make sync-obo-foundry` | Creates or updates OBO Foundry resource pages | `https://obofoundry.org/registry/ontologies.yml` |
| Translator release feed | `util/sync_translator.py` | `make sync-translator` | Updates the [`translator`](../resource/translator/translator.html) resource with the current Translator KGX release products | `https://kgx-storage.rtx.ai/releases/latest-release-summary.json` plus per-release `graph-metadata.json` files under `https://kgx-storage.rtx.ai/releases/<release>/latest/` |

## Notes

- These syncs update source `resource/*.md` files in the repository. They do not write directly to `registry/`, which remains generated output.
- Product detail pages under `resource/<resource-id>/` are generated from resource frontmatter during metadata extraction.
- The OBO Foundry sync has additional documentation in [OBO Foundry Synchronization](obo-foundry-sync.html).
