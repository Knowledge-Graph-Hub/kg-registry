---
layout: graph_visualization
title: KG-Registry Knowledge Graph
description: A graph visualization of the Knowledge Graph Registry resources and their relationships.
permalink: /kg-registry-kg/
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.2.4/pixi.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/kg-registry-kg-visualization.js"></script>
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/kg-registry-kg.css">

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
