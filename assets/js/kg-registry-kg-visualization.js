/**
 * KG-Registry Knowledge Graph Visualization
 * This script renders a force-directed graph of the KG-Registry resources and their relationships
 * using D3.js and PixiJS for high-performance rendering.
 */

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
    Aggregator: "#d62728",
    Resource: "#9467bd",
    Product: "#8c564b",
    GraphProduct: "#e377c2",
    DataModelProduct: "#7f7f7f",
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
let graph = { nodes: [], links: [] };
let simulation;
let svg;
let linkElements, nodeElements, textElements;
let selectedNode = null;
let app, graphContainer;
let pixiNodes = {}, pixiLinks = {};
let pixiContainer;

// Initialize the visualization
document.addEventListener('DOMContentLoaded', () => {
  loadData().then(initializeGraph);
});

/**
 * Load KG-Registry data from kgs.yml
 */
async function loadData() {
  try {
    const response = await fetch('/kg-registry/registry/kgs.yml');
    const text = await response.text();
    const data = jsyaml.load(text);
    
    return processData(data);
  } catch (error) {
    console.error('Error loading data:', error);
    return { nodes: [], links: [] };
  }
}

/**
 * Process the raw data into nodes and links for the graph
 */
function processData(data) {
  const nodes = [];
  const links = [];
  const nodeMap = {};
  
  // Process resources
  if (data && data.resources) {
    // First pass: create nodes for all resources
    data.resources.forEach(resource => {
      if (!resource.id) return;
      
      const node = {
        id: resource.id,
        name: resource.name || resource.id,
        type: resource.category || 'Resource',
        description: resource.description || '',
        url: resource.homepage_url || '',
        domains: resource.domains || []
      };
      
      nodes.push(node);
      nodeMap[resource.id] = node;
      
      // Add products as nodes
      if (resource.products && Array.isArray(resource.products)) {
        resource.products.forEach((product, index) => {
          if (!product.category) return;
          
          const productId = `${resource.id}_product_${index}`;
          const productNode = {
            id: productId,
            name: product.description || `Product ${index}`,
            type: product.category,
            url: product.product_url || '',
            parentId: resource.id
          };
          
          nodes.push(productNode);
          nodeMap[productId] = productNode;
          
          // Create link from resource to product
          links.push({
            source: resource.id,
            target: productId,
            type: 'has_product'
          });
          
          // If this product references other resources
          if (product.original_source && Array.isArray(product.original_source)) {
            product.original_source.forEach(sourceId => {
              if (nodeMap[sourceId]) {
                links.push({
                  source: productId,
                  target: sourceId,
                  type: 'derived_from'
                });
              }
            });
          }
        });
      }
      
      // Add links for related resources
      if (resource.components && Array.isArray(resource.components)) {
        resource.components.forEach(componentId => {
          if (nodeMap[componentId]) {
            links.push({
              source: resource.id,
              target: componentId,
              type: 'has_component'
            });
          }
        });
      }
    });
    
    // Second pass: add domain-based connections
    const domainConnections = {};
    nodes.filter(node => node.domains && node.domains.length > 0)
      .forEach(node => {
        node.domains.forEach(domain => {
          if (!domainConnections[domain]) {
            domainConnections[domain] = [];
          }
          domainConnections[domain].push(node.id);
        });
      });
    
    // Create links between resources in the same domain
    Object.values(domainConnections).forEach(resourceIds => {
      if (resourceIds.length < 2) return;
      
      // Connect resources with the same domain
      for (let i = 0; i < resourceIds.length; i++) {
        for (let j = i + 1; j < resourceIds.length; j++) {
          // Avoid duplicate links
          const existingLink = links.find(link => 
            (link.source === resourceIds[i] && link.target === resourceIds[j]) ||
            (link.source === resourceIds[j] && link.target === resourceIds[i])
          );
          
          if (!existingLink) {
            links.push({
              source: resourceIds[i],
              target: resourceIds[j],
              type: 'shared_domain'
            });
          }
        }
      }
    });
  }
  
  return { nodes, links };
}

/**
 * Initialize the graph visualization
 */
function initializeGraph(data) {
  graph = data;
  
  // If using pure D3
  setupD3Visualization();
  
  // If using PixiJS + D3
  // setupPixiVisualization();
  
  // Setup UI controls
  setupControls();
}

/**
 * Set up the D3.js force-directed graph
 */
function setupD3Visualization() {
  const container = document.getElementById('graph-container');
  const width = container.clientWidth;
  const height = container.clientHeight;
  
  // Create SVG element
  svg = d3.select('#graph-container')
    .append('svg')
    .attr('width', width)
    .attr('height', height);
  
  // Create container for all elements
  const g = svg.append('g');
  
  // Add zoom behavior
  svg.call(d3.zoom()
    .scaleExtent([0.1, 4])
    .on('zoom', (event) => {
      g.attr('transform', event.transform);
    })
  );
  
  // Create link elements
  linkElements = g.append('g')
    .selectAll('line')
    .data(graph.links)
    .enter()
    .append('line')
    .attr('class', 'link')
    .attr('stroke-width', config.links.width.default)
    .attr('stroke-opacity', config.links.opacity.default);
  
  // Create node elements
  nodeElements = g.append('g')
    .selectAll('circle')
    .data(graph.nodes)
    .enter()
    .append('circle')
    .attr('class', 'node')
    .attr('r', config.nodeRadius.default)
    .attr('fill', d => config.colors[d.type] || config.colors.Resource)
    .call(d3.drag()
      .on('start', dragStarted)
      .on('drag', dragging)
      .on('end', dragEnded)
    )
    .on('click', nodeClicked)
    .on('mouseover', nodeMouseOver)
    .on('mouseout', nodeMouseOut);
  
  // Add tooltips using title
  nodeElements.append('title')
    .text(d => `${d.name} (${d.type})\n${d.description || ''}`);
  
  // Create text labels
  textElements = g.append('g')
    .selectAll('text')
    .data(graph.nodes)
    .enter()
    .append('text')
    .text(d => d.name)
    .attr('font-size', 12)
    .attr('dx', 15)
    .attr('dy', 4);
  
  // Create force simulation
  simulation = d3.forceSimulation(graph.nodes)
    .force('link', d3.forceLink(graph.links).id(d => d.id).distance(config.simulation.distance))
    .force('charge', d3.forceManyBody().strength(config.simulation.strength))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .on('tick', ticked);
  
  // Create the legend
  createLegend();
}

/**
 * Tick function for updating positions in D3
 */
function ticked() {
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
}

/**
 * Create a legend for the node types
 */
function createLegend() {
  const legend = d3.select('#graph-legend');
  
  Object.entries(config.colors).forEach(([type, color]) => {
    const item = legend.append('div')
      .attr('class', 'legend-item');
    
    item.append('div')
      .attr('class', 'legend-color')
      .style('background-color', color);
    
    item.append('span')
      .text(type);
  });
}

/**
 * Setup the UI controls for the graph
 */
function setupControls() {
  // Populate node type filter
  const nodeTypes = [...new Set(graph.nodes.map(node => node.type))];
  const typeFilter = document.getElementById('node-type-filter');
  
  nodeTypes.forEach(type => {
    const option = document.createElement('option');
    option.value = type;
    option.textContent = type;
    typeFilter.appendChild(option);
  });
  
  // Add event listeners
  typeFilter.addEventListener('change', filterNodesByType);
  
  document.getElementById('search-input').addEventListener('input', searchNodes);
  document.getElementById('reset-graph').addEventListener('click', resetGraph);
}

/**
 * Filter nodes by type
 */
function filterNodesByType() {
  const selectedType = document.getElementById('node-type-filter').value;
  
  if (selectedType === 'all') {
    nodeElements.style('opacity', 1);
    linkElements.style('opacity', config.links.opacity.default);
    textElements.style('opacity', 1);
    return;
  }
  
  // Set all nodes to semi-transparent
  nodeElements.style('opacity', 0.2);
  linkElements.style('opacity', 0.1);
  textElements.style('opacity', 0.2);
  
  // Highlight selected nodes
  const selectedNodes = graph.nodes.filter(node => node.type === selectedType);
  const selectedNodeIds = new Set(selectedNodes.map(node => node.id));
  
  nodeElements.filter(node => node.type === selectedType)
    .style('opacity', 1);
  
  textElements.filter(node => node.type === selectedType)
    .style('opacity', 1);
  
  // Show links between selected nodes
  linkElements.filter(link => 
    selectedNodeIds.has(link.source.id) && selectedNodeIds.has(link.target.id)
  ).style('opacity', config.links.opacity.default);
}

/**
 * Search for nodes by name or ID
 */
function searchNodes() {
  const searchTerm = document.getElementById('search-input').value.toLowerCase();
  
  if (!searchTerm) {
    nodeElements.style('opacity', 1);
    linkElements.style('opacity', config.links.opacity.default);
    textElements.style('opacity', 1);
    return;
  }
  
  // Set all nodes to semi-transparent
  nodeElements.style('opacity', 0.2);
  linkElements.style('opacity', 0.1);
  textElements.style('opacity', 0.2);
  
  // Highlight matching nodes
  const matchingNodes = graph.nodes.filter(node => 
    node.name.toLowerCase().includes(searchTerm) || 
    node.id.toLowerCase().includes(searchTerm)
  );
  
  const matchingNodeIds = new Set(matchingNodes.map(node => node.id));
  
  nodeElements.filter(node => 
    node.name.toLowerCase().includes(searchTerm) || 
    node.id.toLowerCase().includes(searchTerm)
  ).style('opacity', 1);
  
  textElements.filter(node => 
    node.name.toLowerCase().includes(searchTerm) || 
    node.id.toLowerCase().includes(searchTerm)
  ).style('opacity', 1);
  
  // Show links between matching nodes
  linkElements.filter(link => 
    matchingNodeIds.has(link.source.id) && matchingNodeIds.has(link.target.id)
  ).style('opacity', config.links.opacity.default);
}

/**
 * Reset the graph to its original state
 */
function resetGraph() {
  document.getElementById('node-type-filter').value = 'all';
  document.getElementById('search-input').value = '';
  
  nodeElements.style('opacity', 1);
  linkElements.style('opacity', config.links.opacity.default);
  textElements.style('opacity', 1);
  
  // Reset node sizes and link widths
  nodeElements.attr('r', config.nodeRadius.default);
  linkElements.attr('stroke-width', config.links.width.default);
  
  // Reset simulation
  simulation.alpha(1).restart();
}

/**
 * Handle node click events
 */
function nodeClicked(event, d) {
  if (selectedNode === d) {
    // Deselect if already selected
    selectedNode = null;
    resetHighlighting();
    hideNodeDetails();
  } else {
    selectedNode = d;
    highlightConnections(d);
    showNodeDetails(d);
  }
}

/**
 * Show node details in the side panel
 */
function showNodeDetails(node) {
  const detailsPanel = document.getElementById('node-details-panel');
  const detailsTitle = document.getElementById('details-title');
  const detailsContent = document.getElementById('details-content');
  
  // Set title
  detailsTitle.textContent = node.name;
  
  // Clear previous content
  detailsContent.innerHTML = '';
  
  // Add details
  const details = [
    { label: 'ID', value: node.id },
    { label: 'Type', value: node.type },
    { label: 'Description', value: node.description || 'No description available' }
  ];
  
  if (node.url) {
    details.push({ label: 'URL', value: `<a href="${node.url}" target="_blank">${node.url}</a>` });
  }
  
  if (node.domains && node.domains.length > 0) {
    details.push({ label: 'Domains', value: node.domains.join(', ') });
  }
  
  // Create definition list items
  details.forEach(detail => {
    const dt = document.createElement('dt');
    dt.textContent = detail.label;
    
    const dd = document.createElement('dd');
    dd.innerHTML = detail.value;
    
    detailsContent.appendChild(dt);
    detailsContent.appendChild(dd);
  });
  
  // Show the panel
  detailsPanel.style.display = 'block';
}

/**
 * Hide node details panel
 */
function hideNodeDetails() {
  document.getElementById('node-details-panel').style.display = 'none';
}

/**
 * Highlight a node and its connections
 */
function highlightConnections(node) {
  // Find connected nodes
  const connectedNodeIds = new Set();
  graph.links.forEach(link => {
    if (link.source.id === node.id) {
      connectedNodeIds.add(link.target.id);
    } else if (link.target.id === node.id) {
      connectedNodeIds.add(link.source.id);
    }
  });
  
  // Set all nodes to semi-transparent
  nodeElements.style('opacity', 0.2);
  linkElements.style('opacity', 0.1);
  textElements.style('opacity', 0.2);
  
  // Highlight selected node
  nodeElements.filter(d => d.id === node.id)
    .style('opacity', 1)
    .attr('r', config.nodeRadius.highlighted);
  
  textElements.filter(d => d.id === node.id)
    .style('opacity', 1)
    .attr('font-weight', 'bold');
  
  // Highlight connected nodes
  nodeElements.filter(d => connectedNodeIds.has(d.id))
    .style('opacity', 1);
  
  textElements.filter(d => connectedNodeIds.has(d.id))
    .style('opacity', 1);
  
  // Highlight connections
  linkElements.filter(link => 
    link.source.id === node.id || link.target.id === node.id
  )
    .style('opacity', config.links.opacity.highlighted)
    .attr('stroke-width', config.links.width.highlighted);
}

/**
 * Reset highlighting to default state
 */
function resetHighlighting() {
  nodeElements.style('opacity', 1)
    .attr('r', config.nodeRadius.default);
  
  linkElements.style('opacity', config.links.opacity.default)
    .attr('stroke-width', config.links.width.default);
  
  textElements.style('opacity', 1)
    .attr('font-weight', 'normal');
}

/**
 * Node mouseover event handler
 */
function nodeMouseOver(event, d) {
  if (selectedNode) return; // Don't override selection highlighting
  
  d3.select(this)
    .attr('r', config.nodeRadius.highlighted);
}

/**
 * Node mouseout event handler
 */
function nodeMouseOut(event, d) {
  if (selectedNode) return; // Don't override selection highlighting
  
  d3.select(this)
    .attr('r', config.nodeRadius.default);
}

/**
 * D3 drag started function
 */
function dragStarted(event, d) {
  if (!event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

/**
 * D3 dragging function
 */
function dragging(event, d) {
  d.fx = event.x;
  d.fy = event.y;
}

/**
 * D3 drag ended function
 */
function dragEnded(event, d) {
  if (!event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
