---
activity_status: active
category: DataSource
contacts:
- category: Organization
  contact_details:
  - contact_type: url
    value: https://yoda.yale.edu/about/contact-us/
  label: Yale University Center for Outcomes Research and Evaluation (CORE)
- category: Individual
  label: Harlan M. Krumholz
- category: Individual
  label: Joseph S. Ross
creation_date: '2026-10-05T00:00:00Z'
description: The Yale University Open Data Access (YODA) Project is an independent
  intermediary at Yale that reviews requests from researchers for access to individual
  participant-level clinical trial data and clinical study reports held by industry
  and academic Data Partners, including Johnson & Johnson (Janssen and J&J MedTech),
  Kenvue, SI-BONE and Queen Mary University of London, with Medtronic as an earlier
  partner. Data Partners transfer full jurisdiction over access decisions to the
  YODA Project. Its searchable catalog listed 513 trials as available when checked
  on 2026-10-05. Approved requestors sign a Data Partner-specific data use agreement
  and analyze data on a secure data sharing platform or receive them through Yale
  Secure File Transfer.
domains:
- clinical
- biomedical
- clinical trials
homepage_url: https://yoda.yale.edu/
id: yoda
last_modified_date: '2026-10-05T00:00:00Z'
layout: resource_detail
license:
  id: https://yoda.yale.edu/about/policies-procedures/data-use-agreement/
  label: Controlled access; a signed Data Partner-specific data use agreement is required
name: The YODA Project
products:
- category: GraphicalInterface
  description: The YODA Project web portal, with information on Data Partners, policies,
    the data request process, approved requests and resulting publications.
  format: http
  id: yoda.portal
  name: YODA Project Portal
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://yoda.yale.edu/
- category: GraphicalInterface
  description: Searchable, filterable catalog of clinical trials whose individual
    participant-level data and clinical study reports are available for request,
    listed by ClinicalTrials.gov NCT number and filterable by Data Partner and generic
    drug or device name.
  format: http
  id: yoda.trial-catalog
  name: YODA Trial Catalog
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  - relation_type: prov:wasInfluencedBy
    source: clinicaltrialsgov
  product_url: https://yoda.yale.edu/trials-search/
- category: GraphicalInterface
  description: Listing of approved data requests, with the research proposal, requestor,
    trials requested and status or publications for each project.
  format: http
  id: yoda.approved-requests
  name: YODA Approved Data Requests
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://yoda.yale.edu/request/approved-data-requests/
- category: DocumentationProduct
  description: Description of how data requests are reviewed, covering YODA Project
    review, Data Partner due diligence assessment, external review, data use agreement
    signature and data access, with expected timelines.
  format: http
  id: yoda.request-process
  name: YODA Data Request Review Process
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://yoda.yale.edu/request/data-request-review-process/
- category: DocumentationProduct
  description: YODA Project Data Release Policies and Procedures (January 2025 version),
    the governing document for data request submission, review and data release.
  format: pdf
  id: yoda.data-release-procedures
  name: YODA Project Data Release Policies and Procedures
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://yoda.yale.edu/wp-content/uploads/2022/11/YODA-Project-Data-Release-Procedures-January-2025.pdf
- category: DocumentationProduct
  description: Data use agreements for each Data Partner (Janssen Pharmaceuticals,
    Johnson & Johnson Medical Device and Kenvue Brands LLC), setting terms for data
    access, data use, reporting of safety findings, redistribution and dissemination
    of results.
  format: http
  id: yoda.data-use-agreement
  name: YODA Data Use Agreements
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://yoda.yale.edu/about/policies-procedures/data-use-agreement/
- category: Product
  description: Metrics on YODA Project activity, including submitted requests to
    use Johnson & Johnson data, details of each data request, clinical trial inquiries,
    clinical study report summary requests and trials determined to be unavailable.
  format: http
  id: yoda.metrics
  name: YODA Project Metrics
  original_source:
  - relation_type: prov:hadPrimarySource
    source: yoda
  product_url: https://yoda.yale.edu/metrics/
publications:
- authors:
  - Joseph S. Ross
  - Joanne Waldstreicher
  - Stephen Bamford
  - Jesse A. Berlin
  - Karla Childers
  - Nihar R. Desai
  - Ginger Gamble
  - Cary P. Gross
  - Richard Kuntz
  - Richard Lehman
  - Peter Lins
  - Sandra A. Morris
  - Jessica D. Ritchie
  - Harlan M. Krumholz
  doi: 10.1038/sdata.2018.268
  id: doi:10.1038/sdata.2018.268
  journal: Scientific Data
  preferred: true
  title: Overview and experience of the YODA Project with clinical trial data sharing
    after 5 years
  year: '2018'
- authors:
  - Harlan M. Krumholz
  - Joseph S. Ross
  doi: 10.1001/jama.2011.1459
  id: doi:10.1001/jama.2011.1459
  journal: JAMA
  title: A Model for Dissemination and Independent Analysis of Industry Data
  year: '2011'
synonyms:
- YODA Project
- Yale University Open Data Access Project
- Yale Open Data Access Project
---
# The YODA Project

The Yale University Open Data Access (YODA) Project, based at the Yale Center for Outcomes Research and Evaluation (CORE) and led by Harlan Krumholz and Joseph Ross, is an independent intermediary for sharing clinical trial data. Data Partners give the YODA Project full jurisdiction over decisions about access to their participant-level trial data and clinical study reports. Current partners include Johnson & Johnson (Janssen pharmaceutical and J&J MedTech device trials), Kenvue, SI-BONE and Queen Mary University of London. Medtronic was an earlier partner, whose data were used for independent systematic reviews.

## Accessing Data

Researchers search the [trial catalog](https://yoda.yale.edu/trials-search/) (513 trials listed as available on 2026-10-05), then submit a research proposal. Requests go through YODA Project review for completeness and scientific merit, a due diligence assessment by the Data Partner, and external review if needed. Approved requestors must sign the Data Partner-specific data use agreement. Depending on the partner, data are provided in a secure data sharing platform or through Yale Secure File Transfer. Data are not openly downloadable.

## Transparency

The YODA Project publishes approved data requests, their resulting publications, and metrics on requests, trial inquiries and trials determined to be unavailable.
