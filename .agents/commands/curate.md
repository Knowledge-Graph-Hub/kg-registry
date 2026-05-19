---
description: Curate a given KG-Registry resource page, either by expanding a stub entry or improving an existing page.
argument-hint: [RESOURCE_ID_OR_NAME]
---

Curate the resource specified in $ARGUMENTS.

PREREQUISITE: this workflow must be run from a local clone of the KG-Registry repository. These curation steps depend on editing and validating files in a checked-out working copy.

IMPORTANT: you MUST consult the kg-registry-curation skill for the full workflow.

Use the existing page in `resource/<id>/<id>.md` when one already exists. Keep the work focused on the named resource, validate the file before finishing, and do not edit anything under `registry/`.