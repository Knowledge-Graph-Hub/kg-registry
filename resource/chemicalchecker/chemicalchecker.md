---
activity_status: active
category: DataSource
id: chemicalchecker
layout: resource_detail
name: Chemical Checker
description: >-
  The Chemical Checker (CC) is a data-driven resource of small molecule bioactivity data, organized into five levels of increasing complexity, ranging from chemical properties to clinical outcomes. It is designed to support computational drug discovery tasks.
domains:
  - bioinformatics
  - drug discovery
homepage: http://packages.sbnb-pages.irbbarcelona.org/chemical_checker/
contact:
  - name: Miquel Duran
    email: miquel.duran@irbbarcelona.org
  - name: Patrick Aloy
    email: patrick.aloy@irbbarcelona.org
repository: https://github.com/sbnb-irb/chemical-checker
products:
  - category: Product
    id: chemicalchecker.signatures
    name: Chemical Checker Signatures
    description: Precomputed signatures for small molecules, suitable for machine learning.
    format: hdf5
    product_url: http://packages.sbnb-pages.irbbarcelona.org/chemical_checker/signaturization.html
  - category: ProcessProduct
    id: chemicalchecker.signaturizer
    name: Signaturizer
    description: Software tool for producing bioactivity signature vectors.
    format: python
    product_url: https://github.com/sbnb-irb/signaturizer
  - category: ProgrammingInterface
    id: chemicalchecker.api
    name: Chemical Checker RESTful API
    description: Programmatic interface for Chemical Checker data.
    product_url: https://chemicalchecker.com/api/db/getSignature/
---

# Chemical Checker (CC)

The Chemical Checker (CC) is a data-driven resource of small molecule bioactivity data, organized into five levels of increasing complexity, ranging from chemical properties to clinical outcomes. It is designed to support computational drug discovery tasks.