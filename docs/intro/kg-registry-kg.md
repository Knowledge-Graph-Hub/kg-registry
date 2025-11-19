---
layout: intro_doc
---

# KG-Registry Knowledge Graph

The KG-Registry Knowledge Graph (KG-Registry-KG) provides an interactive visualization of the relationships between resources in the KG-Registry.

## Overview

The KG-Registry-KG allows you to:
- Incrementally build a custom visualization by selecting specific resources
- Explore relationships between resources through their products
- Export visualizations as images or data files
- View example knowledge graphs with a single click

## Accessing the Visualization

Visit the [KG-Registry Knowledge Graph page](/kg-registry/kg-registry-kg/) to access the interactive visualization.

## Features

### Interactive Graph Building

- **Incremental Loading**: Start with an empty graph and add only the resources you want to explore
- **Resource Selection**: Choose resources from a searchable dropdown list (hold Ctrl/Cmd for multiple selections)
- **Direct Connections Only**: Each resource initially shows only its direct products, keeping the graph manageable
- **Right-Click Expansion**: Right-click any node to expand its connections to other resources
- **Example Button**: Click the "Example" button to randomly display a Knowledge Graph resource

### Navigation and Interaction

- **Drag and Reposition**: Drag nodes to arrange them for better visibility
- **Click for Details**: Left-click any node to see its metadata and highlight its connections
- **Zoom and Pan**: Use mouse wheel or pinch gestures to zoom; drag the background to pan
- **Search**: Filter the resource list by name to quickly find specific resources

### Display Customization

The **Display Options** dropdown provides several customization features:
- **Show Products**: Toggle visibility of product nodes
- **Show Domain Connections**: Display connections between resources that share domains
- **Show Icons**: Toggle Bootstrap icons on nodes representing different resource and product types
- **Filter Node Types**: Show only specific types of nodes (e.g., only DataSources)

### Export Capabilities

The **Export Current View** dropdown offers multiple export formats:

**Image Exports:**
- **SVG (Vector)**: Scalable vector graphic suitable for publications and presentations
- **PNG (Raster)**: Raster image for easy sharing and embedding

**Data Exports:**
- **Interactions (TSV)**: Tab-separated file containing all visible edges with source, target, relationship type, and node metadata
- **Resources (YAML)**: YAML file containing complete metadata for all displayed resources (matches registry format)
- **Resources (JSON-LD)**: JSON-LD file with semantic web context for all displayed resources

All exports automatically include the current date in the filename.

## Implementation Details

The visualization loads data from `registry/kgs.yml`, which contains the complete registry of all resources.

Resources are loaded once at initialization, then added to the graph on-demand as users select them.

### Maintenance

When new resources are added to the registry, they automatically appear in the resource selector on the next build. No additional maintenance is required unless:
- New resource/product categories are added (update color scheme and icon mappings in JavaScript)
- New relationship types are added (update link rendering logic)
- The registry data structure changes significantly (update data loading and node creation logic)

## Usage Tips

1. **Start Small**: Begin with 1-3 resources to keep the visualization manageable
2. **Expand Incrementally**: Right-click nodes to expand their connections as needed
3. **Use the Example Button**: Click "Example" to see a random Knowledge Graph and understand the visualization
4. **Search First**: Use the search box to filter the resource list before selecting
5. **Explore Products**: Keep "Show Products" enabled to see how resources produce different types of outputs
6. **Export for Sharing**: Use SVG export for publications, PNG for presentations, TSV for analysis
7. **Track Components**: View the component count to understand if you have multiple disconnected subgraphs
8. **Customize Colors**: Icons can be hidden if you prefer a cleaner look focusing on colors alone

## Related Documentation

- [Resources in the KG-Registry](resources.html)
- [Products in the KG-Registry](products.html)
