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

<div id="node-details-panel" class="node-details">
  <span class="close-details" onclick="hideNodeDetails()">&times;</span>
  <h3 id="details-title">Resource Details</h3>
  <dl id="details-content"></dl>
</div>

<!-- Context menu for nodes -->
<div id="context-menu" class="context-menu" style="display: none;">
  <div class="context-menu-item" id="expand-node">
    <i class="bi bi-arrows-expand"></i> Expand Connections
  </div>
  <div class="context-menu-item" id="hide-node">
    <i class="bi bi-eye-slash"></i> Hide Node
  </div>
</div>

<script>
  function hideNodeDetails() {
    document.getElementById('node-details-panel').style.display = 'none';
  }
</script>
