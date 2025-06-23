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
- Automatic zoom-to-fit behavior to show the entire graph on initial load
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
   - Node names are determined using the following precedence:
     - For resources: the `name` property from kgs.yml, falling back to the resource `id` if not available
     - For products: the `description` property, falling back to the product `id` if not available

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

## Automatic Zoom-to-Fit and Loading Progress

The visualization includes an automatic zoom-to-fit feature that ensures the entire graph is visible:

1. **Initial Load**: When the graph first loads, it automatically calculates the bounding box of all nodes and zooms to fit the entire graph in the view.

2. **After Reset**: When the "Reset Graph" button is clicked, the graph will re-center and zoom to fit all nodes after the simulation stabilizes.

3. **Smooth Transitions**: The zoom-to-fit uses smooth transitions for a better user experience.

4. **Loading Overlay**: A semi-transparent overlay with a message appears while the graph is being built.

5. **Progress Bar**: A progress bar shows the current state of the force-directed layout calculation, giving users feedback during processing of large graphs.

6. **Balanced Zoom Level**: The zoom level is carefully balanced to avoid excessive zoom-out for large graphs or too much zoom-in for small graphs.

This feature helps users get a complete overview of the graph structure before diving into specific sections and provides visual feedback during the loading process.

## Performance Optimizations

Several optimizations have been implemented to improve the visualization performance, especially for larger graphs:

1. **Pre-computed Node Connections**: Connections between nodes are calculated once when the data loads, rather than recomputing them every time a node is selected.

2. **CSS Class-based Styling**: Uses CSS class toggling instead of direct style manipulation for better performance.

3. **Batched DOM Updates**: Uses requestAnimationFrame to batch visual updates for smoother performance.

4. **Efficient DOM Manipulation**: Uses DocumentFragment for building complex DOM structures in memory before adding them to the page.

5. **Reduced DOM Reflows**: Minimizes style recalculations by using CSS transitions for animations.

6. **Optimized Filtering**: Improved algorithms for filtering and highlighting nodes and connections.

These optimizations significantly improve performance when working with large graphs, especially when selecting nodes and highlighting their connections.

## Node Uniqueness Handling

To ensure data integrity and proper visualization, the implementation handles node uniqueness with several mechanisms:

1. **Node Map Tracking**: A `nodeMap` object tracks all created nodes by their IDs to prevent duplicates.

2. **Placeholder Node Creation**: When a node references another node that hasn't been defined yet, a placeholder node is created. This placeholder is later updated with complete information when the referenced node is properly defined.

3. **Smart Duplicate Prevention**: 
   - During data processing, the system checks if a node with the same ID already exists before creating a new one
   - For product nodes, it properly updates existing nodes with additional information instead of creating duplicates
   - For resource nodes, it ensures component relationships are properly established without duplication

4. **Final Validation**: A final validation step ensures no duplicate nodes exist in the final graph by:
   - Using a Set to track unique node IDs
   - Keeping only the first instance of each node
   - Logging warnings about duplicate nodes for debugging
   - Filtering links to ensure they only reference valid nodes

5. **Link Validation**: The system ensures all links reference existing nodes and removes invalid links.

6. **Parent-Child Relationship Validation**: Product nodes with invalid parent references are identified and reported.

This comprehensive approach ensures the graph visualization accurately represents the data without duplication or missing relationships.

## Maintenance

When new resources are added to the registry, the graph will automatically include them on the next build of the site. No additional maintenance is required unless new resource types are added, in which case you may want to update the color scheme in the JavaScript file.
