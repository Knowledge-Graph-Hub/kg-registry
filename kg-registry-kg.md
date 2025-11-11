---
layout: graph_visualization
title: KG-Registry Knowledge Graph
description: An interactive visualization of the Knowledge Graph Registry resources and their relationships.
permalink: /kg-registry-kg/
---

<!-- D3.js and JS-YAML for data loading and graph layout -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js"></script>

<!-- Custom visualization scripts and styles -->
<script src="{{ site.baseurl }}/assets/js/kg-registry-kg-visualization-incremental.js"></script>
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/kg-registry-kg.css">

<div class="row mb-4">
  <div class="col-12">
    <div class="alert alert-info" role="alert">
      <h4 class="alert-heading">How to use this visualization</h4>
      <p>This interactive graph shows the relationships between resources in the KG-Registry. Start by selecting one or more resources to visualize their connections.</p>
      <hr>
      <ul>
        <li><strong>Select resources</strong> from the dropdown list on the right (hold Ctrl/Cmd for multiple selections)</li>
        <li><strong>Click "Add Selected Resources"</strong> to add them to the graph along with their direct connections</li>
        <li><strong>Click on a node</strong> to see its details and highlight its connections</li>
        <li><strong>Drag nodes</strong> to reposition them for better visibility</li>
        <li><strong>Use the checkboxes</strong> to show/hide products and domain-based connections</li>
        <li><strong>Remove resources</strong> by clicking the × button next to their name in the "Active Resources" list</li>
        <li><strong>Zoom</strong> in and out using the mouse wheel or pinch gestures</li>
        <li><strong>Search</strong> for specific resources using the search box to filter the resource list</li>
      </ul>
      <p class="mb-0"><em>Tip: Start with a small number of resources to keep the visualization manageable, then add more as needed.</em></p>
    </div>
  </div>
</div>

<div id="node-details-panel" class="node-details">
  <span class="close-details" onclick="hideNodeDetails()">&times;</span>
  <h3 id="details-title">Resource Details</h3>
  <dl id="details-content"></dl>
</div>

<script>
  function hideNodeDetails() {
    document.getElementById('node-details-panel').style.display = 'none';
  }
</script>
