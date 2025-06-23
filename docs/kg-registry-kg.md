# KG-Registry Knowledge Graph

This feature provides a graph visualization of the KG-Registry resources and their relationships.

## Overview

The KG-Registry Knowledge Graph (KG-Registry-KG) visualizes the relationships between the various resources in the KG-Registry. It uses D3.js for the force-directed graph layout and can optionally use PixiJS for high-performance rendering.

## Files

- `kg-registry-kg.md`: The main page for the KG-Registry-KG
- `_layouts/graph_visualization.html`: The layout template for the visualization page
- `assets/js/kg-registry-kg-visualization.js`: The JavaScript code for the visualization
- `assets/css/kg-registry-kg.css`: The CSS styles for the visualization

## Features

- Interactive force-directed graph of resources and their relationships
- Node color-coding by resource type
- Filtering by resource type
- Search functionality
- Node selection and highlighting of connections
- Detailed information panel for selected nodes
- Zoom and pan capabilities
- Responsive design

## Data Source

The visualization uses data from the `registry/kgs.yml` file, which contains the registry of all resources. The data is processed to create nodes and links for the graph.

## Implementation Details

1. The visualization uses D3.js for layout and rendering
2. Resources from `kgs.yml` are represented as nodes
3. Relationships between resources are represented as links
4. The graph is interactive, allowing users to:
   - Drag nodes
   - Click on nodes to see details
   - Filter nodes by type
   - Search for specific nodes
   - Reset the graph to its original state

## Future Enhancements

Potential future improvements include:

1. Switching to PixiJS for improved performance with large graphs
2. Adding more filtering options (by domain, activity status, etc.)
3. Implementing a more detailed visualization of resource relationships
4. Adding export options for the graph (PNG, SVG, JSON)
5. Creating a fullscreen mode for better exploration

## Maintenance

When new resources are added to the registry, the graph will automatically include them on the next build of the site. No additional maintenance is required unless new resource types are added, in which case you may want to update the color scheme in the JavaScript file.
