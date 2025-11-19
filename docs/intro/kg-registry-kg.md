---
layout: intro_doc
---

# KG-Registry Knowledge Graph

The KG-Registry Knowledge Graph (KG-Registry-KG) provides an interactive visualization of the relationships between resources in the KG-Registry. This feature uses D3.js for force-directed graph layout and rendering, allowing users to explore how resources, their products, and their relationships connect together.

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

### Visual Features

- **Color-Coded Nodes**: Different resource and product types use distinct colors
- **Category Icons**: Bootstrap icons indicate the category of each node (can be toggled off)
- **Bold Borders**: User-selected resources are highlighted with bold black borders
- **Interactive Legend**: Legend shows all node types with their colors and icons
- **Node Labels**: Resource nodes show names; product nodes show IDs (which are typically shorter)

### Graph Management

- **Active Resources List**: Track which resources are currently displayed with removable badges
- **Statistics**: View real-time counts of nodes, edges, and connected components
- **Clear Graph**: Remove all resources and start fresh
- **Context Menu**: Right-click any node for additional options (expand connections, hide node)

## Implementation Details

### Files

- `kg-registry-kg.md`: The main page for the KG-Registry-KG
- `_layouts/graph_visualization.html`: The layout template for the visualization page
- `assets/js/kg-registry-kg-visualization-incremental.js`: The JavaScript code for incremental graph building
- `assets/css/kg-registry-kg.css`: The CSS styles for the visualization

### Data Source

The visualization loads data from `registry/kgs.yml`, which contains the complete registry of all resources. Resources are loaded once at initialization, then added to the graph on-demand as users select them.

### Architecture

1. **Incremental Loading Model**: 
   - Graph starts empty for better performance
   - Resources are added only when explicitly selected
   - Products are created for each added resource
   - Product connections only appear when both the product's parent resource and its source resources are in the graph

2. **Smart Connection Building**:
   - Products link to their parent resources via "has_product" relationships
   - Products link to their source resources via "derived_from" relationships
   - Resources can link to component resources via "has_component" relationships
   - Domain connections show resources that share domains (optional)

3. **Node Identity**:
   - Resources use their resource ID as the node ID
   - Products use their product ID (e.g., `resource.product_name`)
   - Products are marked with a `parentId` property linking them to their resource

4. **Force-Directed Layout**:
   - D3.js force simulation positions nodes automatically
   - Collision detection prevents node overlap
   - Users can drag nodes to manually adjust positions
   - Positions are maintained during updates

5. **Export Implementation**:
   - SVG export clones the current SVG with proper viewBox and background
   - PNG export converts SVG to canvas, then to PNG blob
   - TSV export formats visible links as tab-separated values
   - YAML/JSON-LD exports include complete resource metadata from the registry

## Usage Tips

1. **Start Small**: Begin with 1-3 resources to keep the visualization manageable
2. **Expand Incrementally**: Right-click nodes to expand their connections as needed
3. **Use the Example Button**: Click "Example" to see a random Knowledge Graph and understand the visualization
4. **Search First**: Use the search box to filter the resource list before selecting
5. **Explore Products**: Keep "Show Products" enabled to see how resources produce different types of outputs
6. **Export for Sharing**: Use SVG export for publications, PNG for presentations, TSV for analysis
7. **Track Components**: View the component count to understand if you have multiple disconnected subgraphs
8. **Customize Colors**: Icons can be hidden if you prefer a cleaner look focusing on colors alone

## Performance Considerations

The incremental loading approach significantly improves performance compared to rendering all resources at once:
- Initial page load is fast (empty graph)
- Only selected resources and their immediate connections are rendered
- Large knowledge graphs can be explored without overwhelming the visualization
- Force simulation only recalculates for visible nodes

## Maintenance

When new resources are added to the registry, they automatically appear in the resource selector on the next build. No additional maintenance is required unless:
- New resource/product categories are added (update color scheme and icon mappings in JavaScript)
- New relationship types are added (update link rendering logic)
- The registry data structure changes significantly (update data loading and node creation logic)

## Related Documentation

- [Resources in the KG-Registry](resources.html)
- [Products in the KG-Registry](products.html)
