---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: email
    value: orphan@fda.hhs.gov
  - contact_type: url
    value: https://www.fda.gov/about-fda/office-chief-medical-officer/office-orphan-products-development
  label: FDA Office of Orphan Products Development
creation_date: '2026-10-04T00:00:00Z'
description: The FDA Orphan Drug Designations and Approvals database, maintained by
  the FDA Office of Orphan Products Development (OOPD), lists drugs and biological
  products that have received orphan designation under the Orphan Drug Act for rare
  diseases or conditions, from 1983 to the present. Each record gives the generic
  and trade names, designation date, designated indication, designation status (including
  withdrawal or revocation dates), FDA orphan approval status, approved labeled indication,
  marketing approval date, orphan exclusivity end date and protected indication, and
  sponsor name and address. Indications are free-text and are not coded to a disease
  vocabulary. The full listing held 8,247 records when exported on 2026-10-04.
domains:
- pharmacology
- rare disease
- biomedical
homepage_url: https://www.accessdata.fda.gov/scripts/opdlisting/oopd/
id: fda-orphan-drugs
infores_id: fda-orphan-drug-db
last_modified_date: '2026-10-04T00:00:00Z'
layout: resource_detail
license:
  id: https://www.usa.gov/government-works
  label: U.S. Government Work (public domain)
name: FDA Orphan Drug Designations and Approvals
products:
- category: GraphicalInterface
  description: Web search form for the orphan drug designation database, searchable
    by product name, sponsor, designated indication, and designation or exclusivity
    date range, with results shown as a condensed list, a detailed list, or a downloadable
    spreadsheet.
  format: http
  id: fda-orphan-drugs.search
  name: Orphan Drug Designations and Approvals Search
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orphan-drugs
  product_url: https://www.accessdata.fda.gov/scripts/opdlisting/oopd/
- category: Product
  description: Spreadsheet export of search results (Search_results.xls), produced
    by choosing the "Download Excel file" output format on the search form. Searching
    the full default date range (01/01/1983 to today) with no other filters returns
    the complete listing, about 9 MB and 8,247 records on 2026-10-04, with one row
    per designation and columns for names, designation and approval status, dates,
    indications, exclusivity, and sponsor address. The file is an HTML table served
    with an Excel content type, and it is only returned for a form POST to OOPD_Results.cfm;
    there is no stable direct download URL.
  format: http
  id: fda-orphan-drugs.export
  name: Orphan Drug Designations Spreadsheet Export
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orphan-drugs
  product_url: https://www.accessdata.fda.gov/scripts/opdlisting/oopd/
- category: DocumentationProduct
  description: FDA guidance page on orphan designation for drugs and biological products,
    covering eligibility, how to request designation, incentives, and links to the
    designation database.
  format: http
  id: fda-orphan-drugs.docs
  name: Designating an Orphan Product Documentation
  original_source:
  - relation_type: prov:hadPrimarySource
    source: fda-orphan-drugs
  product_url: https://www.fda.gov/industry/medical-products-rare-diseases-and-conditions/designating-orphan-product-drugs-and-biological-products
synonyms:
- FDA Orphan Drug Designations
- Orphan Drug Product Designation Database
- OOPD database
---
# FDA Orphan Drug Designations and Approvals

The FDA Office of Orphan Products Development (OOPD) maintains a searchable
database of every drug and biological product granted orphan designation since
the Orphan Drug Act of 1983. Records cover the designated indication, designation
and approval status, marketing approval and orphan exclusivity dates, and the
sponsor. The full listing can be exported as a spreadsheet from the search form,
though only through a form submission rather than a fixed download URL. The data
is a U.S. Government work in the public domain. openFDA does not expose an orphan
designation endpoint.
