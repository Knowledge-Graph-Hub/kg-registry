/**
 * KG-Registry Graph Visualization - Incremental Loading Version
 * This version loads resources on-demand, starting with user-selected resources
 * and their direct connections, improving performance for large graphs.
 */

/**
 * Helper function to truncate text with ellipsis
 */
function truncateText(text, maxLength = 20) {
  if (text && text.length > maxLength) {
    return text.substring(0, maxLength - 3) + '...';
  }
  return text;
}

/**
 * Generate a link to the registry page for a node
 */
function generateRegistryLink(node) {
  const id = node.id;
  
  // Check if this is a resource or a product
  if (node.parentId) {
    // This is a product
    const productId = node.id;
    let resourceId = null;
    if (typeof productId === 'string' && productId.includes('.')) {
      resourceId = productId.split('.')[0];
    } else if (typeof productId === 'string' && productId.includes('/')) {
      resourceId = productId.split('/')[0];
    }
    resourceId = resourceId || node.parentId;
    return `<a href="/kg-registry/resource/${resourceId}/${productId}.html">${id}</a>`;
  } else {
    // This is a resource
    return `<a href="/kg-registry/resource/${id}/${id}.html">${id}</a>`;
  }
}

// Configuration
const config = {
  nodeRadius: {
    default: 10,
    highlighted: 15
  },
  colors: {
    KnowledgeGraph: "#ff7f0e",
    DataSource: "#1f77b4",
    DataModel: "#2ca02c",
    Ontology: "#9c27b0",
    Aggregator: "#d62728",
    Resource: "#9467bd",
    Product: "#8c564b",
    GraphProduct: "#e377c2",
    DataModelProduct: "#7f7f7f",
    OntologyProduct: "#ce93d8",
    MappingProduct: "#bcbd22",
    ProcessProduct: "#17becf",
    GraphicalInterface: "#aec7e8",
    ProgrammingInterface: "#ffbb78"
  },
  links: {
    width: {
      default: 1,
      highlighted: 2
    },
    opacity: {
      default: 0.6,
      highlighted: 1
    }
  },
  simulation: {
    strength: -400,
    distance: 100
  }
};

// State
let allResources = []; // All available resources from the data file
let allResourceMap = {}; // Map of resource ID to resource data
let displayedGraph = { nodes: [], links: [] }; // Currently displayed graph
let activeResourceIds = new Set(); // Set of resource IDs currently in the graph
let simulation;
let svg;
let linkElements, nodeElements, textElements;
let selectedNode = null;
let showProducts = true;
let showDomainConnections = false;

// Initialize the visualization
document.addEventListener('DOMContentLoaded', () => {
  loadData().then(data => {
    allResources = data.resources || [];
    buildResourceMap();
    populateResourceSelector();
    setupControls();
    createLegend();
    initializeEmptyGraph();
  });
});

/**
 * Build a map of all resources for quick lookup
 */
function buildResourceMap() {
  allResources.forEach(resource => {
    if (resource.id) {
      allResourceMap[resource.id] = resource;
    }
  });
}

/**
 * Populate the resource selector dropdown
 */
function populateResourceSelector() {
  const selector = document.getElementById('resource-selector');
  selector.innerHTML = '';
  
  // Sort resources alphabetically by name
  const sortedResources = [...allResources].sort((a, b) => {
    const nameA = (a.name || a.id || '').toLowerCase();
    const nameB = (b.name || b.id || '').toLowerCase();
    return nameA.localeCompare(nameB);
  });
  
  sortedResources.forEach(resource => {
    if (!resource.id) return;
    
    const option = document.createElement('option');
    option.value = resource.id;
    option.textContent = `${resource.name || resource.id} (${resource.category || 'Resource'})`;
    selector.appendChild(option);
  });
}

/**
 * Load KG-Registry data from kgs.yml
 */
async function loadData() {
  try {
    const response = await fetch('/kg-registry/registry/kgs.yml');
    const text = await response.text();
    const data = jsyaml.load(text);
    return data;
  } catch (error) {
    console.error('Error loading data:', error);
    return { resources: [] };
  }
}

/**
 * Initialize an empty graph
 */
function initializeEmptyGraph() {
  const container = document.getElementById('graph-container');
  const width = container.clientWidth;
  const height = container.clientHeight;
  
  // Create SVG element
  svg = d3.select('#graph-container')
    .append('svg')
    .attr('width', width)
    .attr('height', height);
  
  // Add zoom behavior
  const zoom = d3.zoom()
    .scaleExtent([0.1, 10])
    .on('zoom', (event) => {
      svg.select('g').attr('transform', event.transform);
    });
  
  svg.call(zoom);
  
  // Create container for graph elements
  svg.append('g').attr('class', 'graph-elements');
  
  // Initialize force simulation
  simulation = d3.forceSimulation([])
    .force('link', d3.forceLink([]).id(d => d.id).distance(config.simulation.distance))
    .force('charge', d3.forceManyBody().strength(config.simulation.strength))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(20));
  
  updateGraph();
}

/**
 * Add resources to the graph
 */
function addResourcesToGraph(resourceIds) {
  resourceIds.forEach(resourceId => {
    if (activeResourceIds.has(resourceId)) {
      return; // Already in graph
    }
    
    const resource = allResourceMap[resourceId];
    if (!resource) {
      console.warn(`Resource ${resourceId} not found`);
      return;
    }
    
    activeResourceIds.add(resourceId);
    
    // Add the resource node
    const resourceNode = {
      id: resource.id,
      name: resource.name || resource.id,
      type: resource.category || 'Resource',
      description: resource.description || '',
      url: resource.homepage_url || '',
      domains: resource.domains || [],
      isUserSelected: true // Mark as user-selected for highlighting
    };
    
    displayedGraph.nodes.push(resourceNode);
    
    // Add products if enabled (but NOT their connected resources automatically)
    if (showProducts && resource.products && Array.isArray(resource.products)) {
      resource.products.forEach((product, index) => {
        if (!product.category) return;
        
        const productId = product.id || `${resource.id}_product_${index}`;
        
        // Check if product already exists
        if (displayedGraph.nodes.find(n => n.id === productId)) {
          return;
        }
        
        const productNode = {
          id: productId,
          name: product.description || productId,
          type: product.category,
          url: product.product_url || '',
          parentId: resource.id,
          isUserSelected: false
        };
        
        displayedGraph.nodes.push(productNode);
        
        // Add link from resource to product
        displayedGraph.links.push({
          source: resource.id,
          target: productId,
          type: 'has_product'
        });
        
        // CHANGED: Don't automatically add connected resources
        // Instead, only add links to resources that are already in the graph
        if (product.original_source && Array.isArray(product.original_source)) {
          product.original_source.forEach(sourceId => {
            // Only create link if the source resource is already in the graph
            if (displayedGraph.nodes.find(n => n.id === sourceId)) {
              displayedGraph.links.push({
                source: productId,
                target: sourceId,
                type: 'derived_from'
              });
            }
          });
        }
      });
    }
    
    // Add component relationships (only if components are already in graph)
    if (resource.components && Array.isArray(resource.components)) {
      resource.components.forEach(componentId => {
        // Only create link if the component is already in the graph
        if (displayedGraph.nodes.find(n => n.id === componentId)) {
          displayedGraph.links.push({
            source: resource.id,
            target: componentId,
            type: 'has_component'
          });
        }
      });
    }
  });
  
  // Add domain connections if enabled
  if (showDomainConnections) {
    addDomainConnections();
  }
  
  updateGraph();
  updateActiveResourcesList();
  updateCounters();
}

/**
 * Add domain-based connections between resources in the graph
 */
function addDomainConnections() {
  const domainMap = {};
  
  // Group resources by domain
  displayedGraph.nodes
    .filter(node => !node.parentId && node.domains && node.domains.length > 0)
    .forEach(node => {
      node.domains.forEach(domain => {
        if (!domainMap[domain]) {
          domainMap[domain] = [];
        }
        domainMap[domain].push(node.id);
      });
    });
  
  // Create connections between resources in the same domain
  Object.values(domainMap).forEach(nodeIds => {
    if (nodeIds.length < 2) return;
    
    for (let i = 0; i < nodeIds.length; i++) {
      for (let j = i + 1; j < nodeIds.length; j++) {
        // Check if link already exists
        const linkExists = displayedGraph.links.find(link =>
          (link.source.id === nodeIds[i] && link.target.id === nodeIds[j]) ||
          (link.source.id === nodeIds[j] && link.target.id === nodeIds[i]) ||
          (link.source === nodeIds[i] && link.target === nodeIds[j]) ||
          (link.source === nodeIds[j] && link.target === nodeIds[i])
        );
        
        if (!linkExists) {
          displayedGraph.links.push({
            source: nodeIds[i],
            target: nodeIds[j],
            type: 'shared_domain'
          });
        }
      }
    }
  });
}

/**
 * Remove a resource from the graph
 */
function removeResourceFromGraph(resourceId) {
  if (!activeResourceIds.has(resourceId)) {
    return;
  }
  
  activeResourceIds.delete(resourceId);
  
  // Remove the resource node and its products
  displayedGraph.nodes = displayedGraph.nodes.filter(node => {
    if (node.id === resourceId) return false;
    if (node.parentId === resourceId) return false;
    return true;
  });
  
  // Remove related links
  const nodeIds = new Set(displayedGraph.nodes.map(n => n.id));
  displayedGraph.links = displayedGraph.links.filter(link => {
    const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
    const targetId = typeof link.target === 'object' ? link.target.id : link.target;
    return nodeIds.has(sourceId) && nodeIds.has(targetId);
  });
  
  updateGraph();
  updateActiveResourcesList();
  updateCounters();
}

/**
 * Clear the entire graph
 */
function clearGraph() {
  activeResourceIds.clear();
  displayedGraph = { nodes: [], links: [] };
  updateGraph();
  updateActiveResourcesList();
  updateCounters();
}

/**
 * Update the graph visualization
 */
function updateGraph() {
  if (!svg) return;
  
  const g = svg.select('g.graph-elements');
  
  // Update simulation with new data
  simulation.nodes(displayedGraph.nodes);
  simulation.force('link').links(displayedGraph.links);
  
  // Update links
  linkElements = g.selectAll('line')
    .data(displayedGraph.links, d => `${d.source.id || d.source}-${d.target.id || d.target}`);
  
  linkElements.exit().remove();
  
  const linkEnter = linkElements.enter()
    .append('line')
    .attr('stroke', '#999')
    .attr('stroke-width', config.links.width.default)
    .attr('stroke-opacity', config.links.opacity.default);
  
  linkElements = linkEnter.merge(linkElements);
  
  // Update nodes
  nodeElements = g.selectAll('circle')
    .data(displayedGraph.nodes, d => d.id);
  
  nodeElements.exit().remove();
  
  const nodeEnter = nodeElements.enter()
    .append('circle')
    .attr('r', config.nodeRadius.default)
    .attr('fill', d => config.colors[d.type] || config.colors.Resource)
    .attr('stroke', d => d.isUserSelected ? '#000' : '#fff')
    .attr('stroke-width', d => d.isUserSelected ? 3 : 1.5)
    .call(d3.drag()
      .on('start', dragStarted)
      .on('drag', dragged)
      .on('end', dragEnded))
    .on('click', (event, d) => {
      event.stopPropagation();
      selectNode(d);
    });
  
  nodeElements = nodeEnter.merge(nodeElements);
  
  // Update node colors and strokes (in case type or selection status changed)
  nodeElements
    .attr('fill', d => config.colors[d.type] || config.colors.Resource)
    .attr('stroke', d => d.isUserSelected ? '#000' : '#fff')
    .attr('stroke-width', d => d.isUserSelected ? 3 : 1.5);
  
  // Update labels
  textElements = g.selectAll('text')
    .data(displayedGraph.nodes, d => d.id);
  
  textElements.exit().remove();
  
  const textEnter = textElements.enter()
    .append('text')
    .attr('font-size', 10)
    .attr('dx', 12)
    .attr('dy', 4)
    .text(d => truncateText(d.name, 15));
  
  textElements = textEnter.merge(textElements);
  
  // Restart simulation
  simulation.alpha(1).restart();
  
  // Update positions on tick
  simulation.on('tick', () => {
    linkElements
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);
    
    nodeElements
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);
    
    textElements
      .attr('x', d => d.x)
      .attr('y', d => d.y);
  });
}

/**
 * Update the active resources list
 */
function updateActiveResourcesList() {
  const listContainer = document.getElementById('active-resources-list');
  
  if (activeResourceIds.size === 0) {
    listContainer.innerHTML = '<small class="text-muted">No resources selected. Choose resources above to visualize their connections.</small>';
    return;
  }
  
  listContainer.innerHTML = '';
  
  Array.from(activeResourceIds).sort().forEach(resourceId => {
    const resource = allResourceMap[resourceId];
    const resourceName = resource ? (resource.name || resourceId) : resourceId;
    
    const badge = document.createElement('span');
    badge.className = 'badge bg-primary me-1 mb-1';
    badge.innerHTML = `${resourceName} <button type="button" class="btn-close btn-close-white" style="font-size: 0.6rem; vertical-align: middle;" aria-label="Remove"></button>`;
    badge.querySelector('button').onclick = () => removeResourceFromGraph(resourceId);
    
    listContainer.appendChild(badge);
  });
}

/**
 * Update node and edge counters
 */
function updateCounters() {
  document.getElementById('node-count').textContent = displayedGraph.nodes.length;
  document.getElementById('edge-count').textContent = displayedGraph.links.length;
}

/**
 * Setup UI controls
 */
function setupControls() {
  // Add resource button
  document.getElementById('add-resource').addEventListener('click', () => {
    const selector = document.getElementById('resource-selector');
    const selectedOptions = Array.from(selector.selectedOptions);
    const selectedIds = selectedOptions.map(option => option.value);
    
    if (selectedIds.length > 0) {
      addResourcesToGraph(selectedIds);
    }
  });
  
  // Clear graph button
  document.getElementById('clear-graph').addEventListener('click', clearGraph);
  
  // Show products checkbox
  document.getElementById('show-products').addEventListener('change', (e) => {
    showProducts = e.target.checked;
    // Rebuild graph with current resources
    const currentResources = Array.from(activeResourceIds);
    clearGraph();
    addResourcesToGraph(currentResources);
  });
  
  // Show domain connections checkbox
  document.getElementById('show-domain-connections').addEventListener('change', (e) => {
    showDomainConnections = e.target.checked;
    // Rebuild graph with current resources
    const currentResources = Array.from(activeResourceIds);
    clearGraph();
    addResourcesToGraph(currentResources);
  });
  
  // Search input for filtering resources
  document.getElementById('search-input').addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const selector = document.getElementById('resource-selector');
    
    Array.from(selector.options).forEach(option => {
      const text = option.textContent.toLowerCase();
      option.style.display = text.includes(searchTerm) ? '' : 'none';
    });
  });
  
  // Node type filter
  const typeFilter = document.getElementById('node-type-filter');
  typeFilter.addEventListener('change', (e) => {
    const filterValue = e.target.value;
    
    if (filterValue === 'all') {
      nodeElements.style('opacity', 1);
      textElements.style('opacity', 1);
    } else {
      nodeElements.style('opacity', d => d.type === filterValue ? 1 : 0.1);
      textElements.style('opacity', d => d.type === filterValue ? 1 : 0.1);
    }
  });
  
  // Populate node type filter
  const types = new Set(['all']);
  Object.keys(config.colors).forEach(type => types.add(type));
  
  types.forEach(type => {
    if (type === 'all') return;
    const option = document.createElement('option');
    option.value = type;
    option.textContent = type;
    typeFilter.appendChild(option);
  });
}

/**
 * Select a node and show its details
 */
function selectNode(node) {
  selectedNode = node;
  
  // Highlight the node and its connections
  nodeElements
    .attr('r', d => d.id === node.id ? config.nodeRadius.highlighted : config.nodeRadius.default)
    .style('opacity', d => {
      if (d.id === node.id) return 1;
      
      // Check if connected
      const isConnected = displayedGraph.links.some(link => {
        const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
        const targetId = typeof link.target === 'object' ? link.target.id : link.target;
        return (sourceId === node.id && targetId === d.id) || 
               (targetId === node.id && sourceId === d.id);
      });
      
      return isConnected ? 1 : 0.2;
    });
  
  linkElements
    .attr('stroke-width', d => {
      const sourceId = typeof d.source === 'object' ? d.source.id : d.source;
      const targetId = typeof d.target === 'object' ? d.target.id : d.target;
      return (sourceId === node.id || targetId === node.id) ? 
        config.links.width.highlighted : config.links.width.default;
    })
    .style('opacity', d => {
      const sourceId = typeof d.source === 'object' ? d.source.id : d.source;
      const targetId = typeof d.target === 'object' ? d.target.id : d.target;
      return (sourceId === node.id || targetId === node.id) ? 
        config.links.opacity.highlighted : 0.2;
    });
  
  // Show node details panel
  showNodeDetails(node);
}

/**
 * Show node details in panel
 */
function showNodeDetails(node) {
  const panel = document.getElementById('node-details-panel');
  const title = document.getElementById('details-title');
  const content = document.getElementById('details-content');
  
  title.textContent = node.name;
  
  content.innerHTML = `
    <dt>ID</dt>
    <dd>${generateRegistryLink(node)}</dd>
    <dt>Type</dt>
    <dd>${node.type}</dd>
    ${node.description ? `<dt>Description</dt><dd>${node.description}</dd>` : ''}
    ${node.url ? `<dt>URL</dt><dd><a href="${node.url}" target="_blank">${node.url}</a></dd>` : ''}
    ${node.domains && node.domains.length > 0 ? `<dt>Domains</dt><dd>${node.domains.join(', ')}</dd>` : ''}
  `;
  
  panel.style.display = 'block';
}

/**
 * Hide node details panel
 */
function hideNodeDetails() {
  document.getElementById('node-details-panel').style.display = 'none';
  selectedNode = null;
  
  // Reset highlighting
  nodeElements.attr('r', config.nodeRadius.default).style('opacity', 1);
  linkElements
    .attr('stroke-width', config.links.width.default)
    .style('opacity', config.links.opacity.default);
}

/**
 * Create legend showing node types and their colors
 */
function createLegend() {
  const legend = document.getElementById('graph-legend');
  legend.innerHTML = '';
  
  // Add note about user-selected resources
  const userSelectedNote = document.createElement('div');
  userSelectedNote.className = 'legend-item mb-3';
  userSelectedNote.innerHTML = `
    <svg width="20" height="20" style="vertical-align: middle;">
      <circle cx="10" cy="10" r="8" fill="#1f77b4" stroke="#000" stroke-width="3" />
    </svg>
    <span class="ms-2"><strong>Bold border = User-selected resource</strong></span>
  `;
  legend.appendChild(userSelectedNote);
  
  // Add horizontal rule
  const hr = document.createElement('hr');
  hr.className = 'my-2';
  legend.appendChild(hr);
  
  // Add node type colors
  Object.entries(config.colors).forEach(([type, color]) => {
    const item = document.createElement('div');
    item.className = 'legend-item mb-2';
    item.innerHTML = `
      <svg width="20" height="20" style="vertical-align: middle;">
        <circle cx="10" cy="10" r="8" fill="${color}" />
      </svg>
      <span class="ms-2">${type}</span>
    `;
    legend.appendChild(item);
  });
}

// Drag functions
function dragStarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

function dragEnded(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

// Click on background to deselect
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('graph-container');
  if (container) {
    container.addEventListener('click', (event) => {
      if (event.target === container || event.target.tagName === 'svg') {
        hideNodeDetails();
      }
    });
  }
});
