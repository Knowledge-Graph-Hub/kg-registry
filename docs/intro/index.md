---
layout: intro_doc
---

# Intro to KG-Registry

## What is a Knowledge Graph?

A knowledge graph, or KG, is a collection of data elements (also called _entities_ or _nodes_) and their relationships (also called _edges_). KGs are often heterogenous, containing multiple types of data from many sources. Definitions vary regarding what makes a graph a KG, but all KGs involve some measure of data integration and modeling the connections among data.

For more on this, see [Ehrlinger and Wöß 2016.](https://ceur-ws.org/Vol-1695/paper4.pdf)

## What is the KG-Registry?

The Knowledge Graph Registry is intended to provide metadata about knowledge graphs, their sources, and their contents.

## What types of things are in the Registry?

- **Resources**: These represent top-level entries for knowledge graph and data sources. [More detail here.](resources.html)
- **Products**: Specific representations or interfaces for a resource (e.g., graph dumps, APIs, or visualizations). This also includes associated software for processing and transforming data. [More detail here.](products.html)

## How can each of these things be viewed?

The [main list](https://kghub.org/kg-registry/) contains resources. 

These may be filtered based on their domain and type.

Select the ID for a Resource to view its page. In addition to its top-level metadata (e.g., links to its homepage), this page contains a list of contacts, relevant publications, use cases, and Products.

Select the ID for a Product to view its page. This page contains metadata about the Product, including its sources.

### Interactive Knowledge Graph Visualization

The [KG-Registry Knowledge Graph](/kg-registry/kg-registry-kg/) provides an interactive visualization that allows you to explore relationships between resources, their products, and their connections. You can:
- Build custom visualizations by selecting specific resources
- Expand connections to see how resources relate to each other
- Export visualizations as images or data files
- See example knowledge graphs with a single click

For more details, see the [KG-Registry-KG documentation](../kg-registry-kg.html).

## How are Registry identifiers created?

Registry identifiers are unique, i.e., `kg-microbe` will always refer to the same Resource.

Products have a flexible identifier structure, but are similarly unique, and are always preceded by the Resource they are produced by.

For example, if a resource named `dataplace` produces a dataset named "genes", the Registry may assign this Product the identifier `dataplace.genes`. If another resource named `datacruncher` processes that data further, however, the Registry may assign this Product the identifier `datacruncher.dataplace.genes`. The Product will be visible on the Resource pages for both `dataplace` and `datacruncher`.

## How are new resources added or updated?

Please [open an issue on the Registry's GitHub page](https://github.com/Knowledge-Graph-Hub/kg-registry/issues/new/choose) to request addition of new resources or updates to existing metadata.

## Who manages the Registry?

The KG-Registry is built and managed by members of the [Berkeley Bioinformatics Open-source Projects (BBOP) group](https://berkeleybop.github.io/) at the [Lawrence Berkeley National Laboratory](https://www.lbl.gov/).

## Who may I contact with questions?

Please [email Harry Caufield](mailto:jhc@lbl.gov) with any questions about the KG-Registry.
