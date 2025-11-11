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
    <div class="card">
      <div class="card-header d-flex justify-content-between align-items-center" style="cursor: pointer;" onclick="toggleHelp()">
        <h4 class="mb-0"><i class="bi bi-info-circle"></i> How to use this visualization</h4>
        <span id="help-toggle-icon">−</span>
      </div>
      <div class="card-body" id="help-content">
        <p>This interactive graph shows the relationships between resources in the KG-Registry. Start by selecting one or more resources to visualize their connections.</p>
        <hr>
        <div class="row">
          <div class="col-md-6">
            <h5>Getting Started</h5>
            <ul>
              <li><strong>Select resources</strong> from the dropdown list on the right (hold Ctrl/Cmd for multiple selections)</li>
              <li><strong>Click "Add Selected Resources"</strong> to add them to the graph</li>
              <li>Each resource will show <strong>only its direct products</strong> by default</li>
            </ul>
          </div>
          <div class="col-md-6">
            <h5>Interacting with the Graph</h5>
            <ul>
              <li><strong>Click on a node</strong> to see its details and highlight its connections</li>
              <li><strong>Drag nodes</strong> to reposition them for better visibility</li>
              <li><strong>Zoom</strong> in and out using the mouse wheel or pinch gestures</li>
            </ul>
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-md-6">
            <h5>Customizing the View</h5>
            <ul>
              <li><strong>Show/hide products</strong> using the checkbox in Display Options</li>
              <li><strong>Show domain connections</strong> to see resources that share domains</li>
              <li><strong>Search</strong> for specific resources using the search box</li>
            </ul>
          </div>
          <div class="col-md-6">
            <h5>Managing Resources</h5>
            <ul>
              <li><strong>Remove resources</strong> by clicking the × button next to their name</li>
              <li><strong>Clear all</strong> resources with the "Clear Graph" button</li>
              <li><strong>User-selected resources</strong> are highlighted with bold black borders</li>
            </ul>
          </div>
        </div>
        <div class="alert alert-info mt-3 mb-0">
          <strong>💡 Tip:</strong> Start with 1-3 resources to keep the visualization manageable. Add more resources to see how they connect. Products only show connections to resources that are already in the graph.
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  function toggleHelp() {
    const content = document.getElementById('help-content');
    const icon = document.getElementById('help-toggle-icon');
    
    if (content.style.display === 'none') {
      content.style.display = 'block';
      icon.textContent = '−';
    } else {
      content.style.display = 'none';
      icon.textContent = '+';
    }
  }
</script>

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
