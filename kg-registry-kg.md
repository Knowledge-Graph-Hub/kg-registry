---
layout: graph_visualization
title: KG-Registry Knowledge Graph
description: An interactive visualization of the Knowledge Graph Registry resources and their relationships.
permalink: /kg-registry-kg/
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.2.4/pixi.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/kg-registry-kg-visualization.js"></script>
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/kg-registry-kg.css">

<div class="row mb-4">
  <div class="col-12">
    <div class="alert alert-info" role="alert">
      <h4 class="alert-heading">How to use this visualization</h4>
      <p>This interactive graph shows the relationships between resources in the KG-Registry. Each node represents a resource or product, and links represent relationships between them.</p>
      <hr>
      <ul>
        <li><strong>Click and drag</strong> nodes to reposition them</li>
        <li><strong>Click</strong> on a node to see its details and highlight its connections</li>
        <li><strong>Use the controls</strong> on the right to filter by node type or search for specific resources</li>
        <li><strong>Click "KGs Only"</strong> to focus only on Knowledge Graph nodes and their connections</li>
        <li><strong>Zoom</strong> in and out using the mouse wheel or pinch gestures</li>
      </ul>
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
