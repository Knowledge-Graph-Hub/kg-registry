---
layout: intro_doc
---

# Resources

All Resources have the following attributes:

- `name`: Human-readable name (required)
- `description`: Detailed description
- `homepage_url`: Primary resource URL
- `repository`: Version control repository
- `license`: Resource licensing information
- `version`: Resource version
- `domain`: Primary scientific domain (see _Domains_ below)
- `contacts`: List of contact points
- `products`: Specific representations of the resource
- `activity_status`: Current state of the resource (active, inactive, etc.)
- `tags`: Categorization tags
- `funding`: Funding source information

## Specialized Resource Types

Each Resource may have a more specific type.

### KnowledgeGraph

A specialized Resource for graph-based data:
- Tracks graph creation and modification dates
- Lists contributors and components
- Represents nodes and edges data collection

### DataSource

This Resource provides data. The data may or may not be in a graph structure.

### DataModel

This Resource defines a data structure or ontology.

### Aggregator

This Resource combines multiple data sources.

## Domains

Resources may cover one of the following domains:

- **upper**: The upper-level domain, for general-purpose data representation and integration.
- **anatomy and development**: The anatomy and development of organisms.
- **health**: The health and diseases of organisms.
- **phenotype**: The phenotypes of organisms.
- **investigations**: Research investigations into specific topics.
- **environment**: The environment and ecosystems.
- **chemistry and biochemistry**: The chemical and biochemical sciences.
- **microbiology**: The microbiological sciences.
- **agriculture**: The agricultural sciences.
- **nutrition**: The nutritional sciences, including diet and metabolomics.
- **biological systems**: The biological sciences and systems.
- **information technology**: The information technology sciences.
- **organisms**: Specific organisms.
- **simulation**: Simulation and modeling of specific phenomena.
- **other**: Another domain not defined here.
