---
layout: intro_doc
---

# Resource Classes

## Resource

The core class for describing knowledge graph resources:

### Key Attributes
- `name`: Human-readable name (required)
- `description`: Detailed description
- `homepage_url`: Primary resource URL
- `repository`: Version control repository
- `license`: Resource licensing information
- `version`: Resource version
- `domain`: Primary scientific domain
- `contacts`: List of contact points
- `products`: Specific representations of the resource

### Status Tracking
- `activity_status`: Current state of the resource (active, inactive, etc.)
- `tags`: Categorization tags
- `funding`: Funding source information

## KnowledgeGraph

A specialized `Resource` for graph-based data:
- Tracks graph creation and modification dates
- Lists contributors and components
- Represents nodes and edges data collection

## DataSource, DataModel, Aggregator

Specialized resource types:
- `DataSource`: Originates data
- `DataModel`: Defines data structure or ontology
- `Aggregator`: Combines multiple data sources