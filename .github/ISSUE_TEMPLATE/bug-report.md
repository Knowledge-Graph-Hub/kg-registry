name: Bug report
description: Create a report to help us improve KG-Registry
labels: [ bug ]

body:
  - type: markdown
    attributes:
      value: This is the form for reporting a bug or technical issue with the KG-Registry site.
  - type: input
    id: description
    attributes:
      label: Description
      description: Please provide a concise description of the bug.
      placeholder: e.g., site is broken on Firefox
    validations:
      required: true
  - type: input
    id: reproduce
    attributes:
      label: Reproduce
      description: What steps may be taken to reproduce the behavior?
      placeholder: e.g., open site on Firefox
    validations:
      required: false
  - type: input
    id: expectations
    attributes:
      label: Expectations
      description: Please describe what you expected to happen instead of encountering the bug.
      placeholder: e.g., expected site to load on Firefox
    validations:
      required: false
  - type: input
    id: details
    attributes:
      label: Details
      description: Please provide any other context for the problem here.
    validations:
      required: false
