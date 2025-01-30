name: Request new resource
description: Request addition of something new to the registry, including knowledge graphs, data models, mappings, or beyond.
title: Add this resource - [Name Here]
labels: [ New ]

body:
  - type: markdown
    attributes:
      value: This is the form for requesting a new resource (e.g., a knowledge graph) in KG-Registry.
  - type: dropdown
    id: resource_type
    attributes:
      label: Resource Type
      description: What kind of resource is this?
      multiple: false
      options:
        - Knowledge Graph
        - Data Source
        - Data Model
        - Mappings
        - Other
    validations:
      required: true
  - type: input
    id: name
    attributes:
      label: Name
      description: What is the name of this entity? An acronym or short phrase works best.
      placeholder: e.g., KG-Tofu
    validations:
      required: true
  - type: input
    id: description
    attributes:
      label: Description
      description: What is the description of this entity, in a sentence or two at most?
      placeholder: e.g., A graph describing knowledge about soy milk curds.
    validations:
      required: true
  - type: input
    id: contributor_name
    attributes:
      label: Contributor Name
      description: What is your name? This will be used for attribution.
      placeholder: e.g., Tabatha Butterscotch
    validations:
      required: true
  - type: input
    id: contributor_github
    attributes:
      label: Contributor GitHub
      description: What is your GitHub name, without the @ symbol?
      placeholder: e.g., tbuttersco
    validations:
      required: true
  - type: input
    id: contributor_orcid
    attributes:
      label: Contributor ORCID
      description: What is your ORCID iD?
      placeholder: e.g., 0000-0001-2345-6789
    validations:
      required: false