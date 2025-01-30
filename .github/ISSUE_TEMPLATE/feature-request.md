name: Feature request
description: Suggest a new feature to add to the KG-Registry site
labels: [ enhancement ]

body:
  - type: markdown
    attributes:
      value: This is the form for suggesting a new feature to add to the KG-Registry site.
  - type: input
    id: description
    attributes:
      label: Description
      description: What feature would you like to see added?
      placeholder: e.g., more colors
    validations:
      required: true
