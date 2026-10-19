---
activity_status: active
category: DataSource
collection:
- nams
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://hpscreg.eu/contact
  label: Fraunhofer Institute for Biomedical Engineering (IBMT)
creation_date: '2026-10-19T00:00:00Z'
description: The Human Pluripotent Stem Cell Registry (hPSCreg) is a global public
  registry and data portal for human embryonic stem cell (hESC) and human induced
  pluripotent stem cell (hiPSC) lines. Registered lines receive a standard name and
  unique identifier, and their records cover donor and derivation information, ethical
  provenance and consent, culture conditions, genetic and characterization data, and
  links to other databases such as BioSamples. Lines are checked by curators before
  release, and hPSCreg issues certificates of ethical provenance and pluripotency.
  The registry also holds research project registrations and a database of clinical
  studies that use hPSC-derived cells. It was founded with European Commission funding
  and is operated by the Fraunhofer Institute for Biomedical Engineering (IBMT).
domains:
- cell biology
- biological systems
- biomedical
- clinical trials
- clinical
homepage_url: https://hpscreg.eu/
id: hpscreg
last_modified_date: '2026-10-19T00:00:00Z'
layout: resource_detail
license:
  id: https://hpscreg.eu/terms
  label: hPSCreg Terms of Use (German copyright law; reproduction outside copyright
    limits requires written consent)
name: Human Pluripotent Stem Cell Registry (hPSCreg)
products:
- category: GraphicalInterface
  description: Web portal for searching and browsing registered hESC and hiPSC lines,
    with a page per line covering donor, derivation, ethics, culture and characterization
    data, plus browse views by provider, research project, country, disease, publication
    and clinical study.
  format: http
  id: hpscreg.portal
  is_public: true
  name: hPSCreg web portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hpscreg
  product_url: https://hpscreg.eu/search?q
- category: ProgrammingInterface
  description: Names API returning a JSON list of all released hPSCreg cell line names,
    with cell type, ontology term, synonyms and identifiers in other databases such
    as BioSamples, and lookup of the hPSCreg name for a given synonym or external
    identifier.
  format: json
  id: hpscreg.names-api
  is_public: true
  name: hPSCreg Names API
  original_source:
  - relation_type: prov:hadPrimarySource
    source: hpscreg
  product_url: https://hpscreg.eu/api/names
publications:
- authors:
  - Stefanie Seltmann
  - Fritz Lekschas
  - Robert Müller
  - Harald Stachelscheid
  - Marie-Sophie Bittner
  - Weiping Zhang
  - Luam Kidane
  - Anna Seriola
  - Anna Veiga
  - Glyn Stacey
  - Andreas Kurtz
  doi: 10.1093/nar/gkv963
  id: https://doi.org/10.1093/nar/gkv963
  journal: Nucleic Acids Research
  preferred: true
  title: hPSCreg--the human pluripotent stem cell registry
  year: '2016'
- authors:
  - Andreas Kurtz
  - Nancy Mah
  - Ying Chen
  - Antonie Fuhr
  - Sabine Kobold
  - Stefanie Seltmann
  - Sabine C. Müller
  doi: 10.1111/cpr.13238
  id: https://doi.org/10.1111/cpr.13238
  journal: Cell Proliferation
  title: 'Human pluripotent stem cell registry: Operations, role and current directions'
  year: '2022'
---
# Human Pluripotent Stem Cell Registry (hPSCreg)

## Overview

hPSCreg is a global registry for human pluripotent stem cell (hPSC) lines, covering
both human embryonic stem cell (hESC) and human induced pluripotent stem cell (hiPSC)
lines. It began in 2007 as a European Commission-funded European hESC registry and
was later broadened to all hPSC lines. It is operated by the Fraunhofer Institute for
Biomedical Engineering (IBMT) in Sulzbach, Germany.

Registration gives each line a standard name and unique identifier, verifies its
ethical provenance and evidence of pluripotency against community criteria, and makes
the line visible to other researchers. hPSCreg names are used as cross-references by
other cell line resources; for example, Cellosaurus records link to the matching
hPSCreg entry.

## Data Content

- Cell line records for hESC and hiPSC lines: provider, donor, derivation method,
  culture conditions, genetic constitution, characterization and use.
- Ethics and consent information for each line, and certificates of ethical
  provenance and pluripotency for certified lines.
- Links to external databases, such as BioSamples identifiers for banked lines.
- Registered research projects that use hPSC lines.
- A database of clinical studies that use hPSC-derived cells.
- An OWL-formatted hPSCreg Cell Line Ontology (HCLO), queryable with SPARQL.

## Access

- Web portal: https://hpscreg.eu/
- Names API (JSON): https://hpscreg.eu/api/names
- Registering lines requires an account; browsing released lines does not.
- The hPSCreg API page notes that export and API mechanisms are being consolidated
  and some data exchanges are disabled for now. In October 2026 the site was
  returning a temporary "service unavailable" message.

## License

The hPSCreg Terms of Use place site content under German copyright law. Reproduction,
adaptation and distribution outside the limits of copyright require the written consent
of the author, and downloads and copies of the pages are permitted only for private,
non-commercial use. No open data license is stated.
