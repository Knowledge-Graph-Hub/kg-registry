---
layout: schema_doc
mermaid: true
---



# Enum: LicenseRestrictivenessEnum 




_A coarse ordering of licenses from least to most restrictive. It is used to choose which source license an aggregate resource inherits when it declares none of its own. Values are listed here from least to most restrictive._




URI: [kgr:LicenseRestrictivenessEnum](https://w3id.org/bridge2ai/data-sheets-schema/LicenseRestrictivenessEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| public domain | None | No rights reserved |
| permissive | None | Reuse with attribution and no further conditions |
| copyleft | None | Reuse under the same or a compatible license |
| non-commercial | None | Reuse for non-commercial or academic purposes only |
| no derivatives | None | Redistribution without modification only |
| custom | None | Bespoke terms that could not be placed on the ladder: terms of use, subscript... |




## Slots

| Name | Description |
| ---  | --- |
| [restrictiveness](restrictiveness.html) | Where this license sits on the restrictiveness ladder used to choose among so... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema






## LinkML Source

<details>
```yaml
name: LicenseRestrictivenessEnum
description: A coarse ordering of licenses from least to most restrictive. It is used
  to choose which source license an aggregate resource inherits when it declares none
  of its own. Values are listed here from least to most restrictive.
from_schema: https://w3id.org/knowledge-graph-hub/kg_registry_schema
rank: 1000
permissible_values:
  public domain:
    text: public domain
    description: No rights reserved. CC0, the Public Domain Mark, and works of the
      U.S. federal government.
  permissive:
    text: permissive
    description: Reuse with attribution and no further conditions. CC BY, MIT, BSD,
      Apache, ODC-By.
  copyleft:
    text: copyleft
    description: Reuse under the same or a compatible license. CC BY-SA, ODbL, and
      the GPL family.
  non-commercial:
    text: non-commercial
    description: Reuse for non-commercial or academic purposes only. CC BY-NC, CC
      BY-NC-SA, and academic-use licenses.
  no derivatives:
    text: no derivatives
    description: Redistribution without modification only. CC BY-ND and CC BY-NC-ND.
  custom:
    text: custom
    description: 'Bespoke terms that could not be placed on the ladder: terms of use,
      subscriptions, controlled access, and mixed or varying licenses. Ranked most
      restrictive because the terms must be read before any reuse.'

```
</details>

