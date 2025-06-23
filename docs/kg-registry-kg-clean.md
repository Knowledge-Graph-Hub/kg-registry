# KG-Registry Knowledge Graph

This feature provides a graph visualization of the KG-Registry resources and their relationships.

## Overview

The KG-Registry Knowledge Graph (KG-Registry-KG) visualizes the relationships between the various resources in the KG-Registry. It uses D3.js for the force-directed graph layout and rendering.

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
- "KGs Only" button to filter and show only KnowledgeGraph nodes and their connections
- Responsive design

## Data Source

The visualization uses data from the `registry/kgs.yml` file, which contains the registry of all resources. The data is processed to create nodes and links for the graph.

## Implementation Details

1. **Visualization System:**
   - D3.js for force-directed graph layout and SVG rendering

2. **Data Processing:**
   - Resources from `kgs.yml` are represented as nodes
   - Relationships between resources are represented as links
   - Product nodes use their registry IDs for consistent linking

3. **Interactive Features:**
   - Drag nodes to reposition them
   - Click nodes to see details and highlight connections
   - Filter nodes by type
   - Search for specific nodes by name or ID
   - Reset the graph to its original state
   - Focus only on Knowledge Graph resources

4. **Accessibility Improvements:**
   - Truncated labels with full information in tooltips
   - High-contrast color scheme
   - Keyboard navigation support
   - Responsive design for various screen sizes

## Usage Tips

- Use the "KGs Only" button to focus specifically on Knowledge Graph resources
- Use the search feature to quickly find specific nodes by name or ID
- Click on node IDs in the details panel to navigate to the corresponding registry page
- Drag nodes to arrange the graph in a way that makes sense for your exploration

## Maintenance

When new resources are added to the registry, the graph will automatically include them on the next build of the site. No additional maintenance is required unless new resource types are added, in which case you may want to update the color scheme in the JavaScript file.
