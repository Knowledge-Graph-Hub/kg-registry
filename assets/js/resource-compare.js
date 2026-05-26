(function () {
  const state = {
    resources: [],
    resourceMap: new Map()
  };

  function getBaseUrl() {
    const baseUrl = window.kgRegistryBaseUrl || '';
    return baseUrl === '/' ? '' : baseUrl;
  }

  function registryPath(path) {
    return `${getBaseUrl()}${path}`;
  }

  function escapeHtml(value) {
    return String(value ?? '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function normalize(value) {
    return String(value ?? '').trim().toLowerCase();
  }

  function sourceAssociationId(sourceAssociation) {
    if (typeof sourceAssociation === 'string') {
      return sourceAssociation.trim();
    }
    if (sourceAssociation && typeof sourceAssociation === 'object' && typeof sourceAssociation.source === 'string') {
      return sourceAssociation.source.trim();
    }
    return '';
  }

  function collectDomains(resource) {
    return new Set((resource && Array.isArray(resource.domains) ? resource.domains : []).filter(Boolean).map(domain => String(domain).trim()));
  }

  function collectOriginalSources(resource) {
    const originalSources = new Set();
    const products = resource && Array.isArray(resource.products) ? resource.products : [];

    products.forEach(product => {
      if (!product || !Array.isArray(product.original_source)) return;
      product.original_source.forEach(sourceAssociation => {
        const sourceId = sourceAssociationId(sourceAssociation);
        if (sourceId) {
          originalSources.add(sourceId);
        }
      });
    });

    return originalSources;
  }

  function setIntersection(left, right) {
    const result = [];
    left.forEach(value => {
      if (right.has(value)) {
        result.push(value);
      }
    });
    return result.sort((a, b) => a.localeCompare(b));
  }

  function setUnion(left, right) {
    return new Set([...left, ...right]);
  }

  function compareResources(leftResource, rightResource) {
    const leftDomains = collectDomains(leftResource);
    const rightDomains = collectDomains(rightResource);
    const leftSources = collectOriginalSources(leftResource);
    const rightSources = collectOriginalSources(rightResource);
    const leftCategory = normalize(leftResource && leftResource.category);
    const rightCategory = normalize(rightResource && rightResource.category);

    const sharedDomains = setIntersection(leftDomains, rightDomains);
    const sharedOriginalSources = setIntersection(leftSources, rightSources);
    const sharedCategory = leftCategory && leftCategory === rightCategory ? leftResource.category : '';

    const domainUnion = setUnion(leftDomains, rightDomains);
    const sourceUnion = setUnion(leftSources, rightSources);
    const categoryUnionSize = sharedCategory ? 1 : 2;

    const weightedShared = sharedDomains.length * 2 + sharedOriginalSources.length * 3 + (sharedCategory ? 4 : 0);
    const weightedUnion = domainUnion.size * 2 + sourceUnion.size * 3 + categoryUnionSize * 4;
    const similarityScore = weightedUnion ? Number(((weightedShared / weightedUnion) * 100).toFixed(1)) : 0;

    return {
      similarityScore,
      sharedDomains,
      sharedOriginalSources,
      sharedCategory,
      leftDomains,
      rightDomains,
      leftSources,
      rightSources,
      sharedFeatureCount: sharedDomains.length + sharedOriginalSources.length + (sharedCategory ? 1 : 0)
    };
  }

  function getResourceUrl(resourceId) {
    return registryPath(`/resource/${encodeURIComponent(resourceId)}/${encodeURIComponent(resourceId)}.html`);
  }

  function getSourceUrl(sourceId) {
    if (!sourceId) return '#';
    const firstSegment = sourceId.includes('.') ? sourceId.split('.')[0] : sourceId.includes('/') ? sourceId.split('/')[0] : sourceId;
    return registryPath(`/resource/${encodeURIComponent(firstSegment)}/${encodeURIComponent(sourceId)}.html`);
  }

  function formatResourceLabel(resource) {
    return resource.name ? `${resource.name} (${resource.id})` : resource.id;
  }

  function categoryIcon(category) {
    const categoryIcons = {
      Aggregator: 'grid-3x3',
      Resource: 'archive',
      KnowledgeGraph: 'globe',
      DataSource: 'shop',
      DataModel: 'diagram-3',
      Ontology: 'diagram-2',
      GraphProduct: 'globe',
      Product: 'box',
      MappingProduct: 'map',
      ProcessProduct: 'gear',
      DataModelProduct: 'diagram-3',
      OntologyProduct: 'diagram-2',
      GraphicalInterface: 'window',
      ProgrammingInterface: 'code-square',
      DocumentationProduct: 'journal-text'
    };

    return categoryIcons[category] || 'box';
  }

  function categoryLabel(category) {
    const categoryLabels = {
      Aggregator: 'Aggregator',
      Resource: 'Resource',
      KnowledgeGraph: 'Knowledge Graph',
      DataSource: 'Data Source',
      DataModel: 'Data Model',
      Ontology: 'Ontology',
      GraphProduct: 'Graph Product',
      Product: 'Product',
      MappingProduct: 'Mapping Product',
      ProcessProduct: 'Process Product',
      DataModelProduct: 'Data Model Product',
      OntologyProduct: 'Ontology Product',
      GraphicalInterface: 'Graphical Interface',
      ProgrammingInterface: 'Programming Interface',
      DocumentationProduct: 'Documentation Product'
    };

    return categoryLabels[category] || category || 'Resource';
  }

  function renderChipList(values, emptyLabel, makeHref) {
    if (!values.length) {
      return `<span class="text-muted">${escapeHtml(emptyLabel)}</span>`;
    }

    return `<div class="compare-chip-list">${values.map(value => {
      const label = escapeHtml(value);
      const href = makeHref ? makeHref(value) : null;
      if (href && href !== '#') {
        return `<a class="compare-chip text-decoration-none" href="${href}">${label}</a>`;
      }
      return `<span class="compare-chip">${label}</span>`;
    }).join('')}</div>`;
  }

  function renderResourceCard(resource) {
    const domains = collectDomains(resource);
    const originalSources = collectOriginalSources(resource);
    const productCount = Array.isArray(resource.products) ? resource.products.length : 0;
    const homepageUrl = resource.homepage_url ? `<a href="${escapeHtml(resource.homepage_url)}" target="_blank" rel="noreferrer">Homepage</a>` : '<span class="text-muted">No homepage listed</span>';

    return `
      <div class="card h-100 compare-card shadow-sm">
        <div class="card-body">
          <div class="d-flex justify-content-between gap-3 align-items-start mb-3">
            <div>
              <div class="text-uppercase small compare-muted fw-semibold mb-1">${escapeHtml(resource.category || 'Resource')}</div>
              <h3 class="h4 mb-1">${escapeHtml(resource.name || resource.id)}</h3>
              <div class="font-monospace text-muted">${escapeHtml(resource.id)}</div>
            </div>
            <a class="btn btn-outline-secondary btn-sm" href="${getResourceUrl(resource.id)}">Open page</a>
          </div>
          <p class="mb-3">${escapeHtml(resource.description || 'No description available.')}</p>
          <div class="row g-3 mb-3">
            <div class="col-sm-4">
              <div class="p-3 rounded-3 bg-light h-100">
                <div class="small compare-muted">Domains</div>
                <div class="fw-semibold">${domains.size}</div>
              </div>
            </div>
            <div class="col-sm-4">
              <div class="p-3 rounded-3 bg-light h-100">
                <div class="small compare-muted">Original sources</div>
                <div class="fw-semibold">${originalSources.size}</div>
              </div>
            </div>
            <div class="col-sm-4">
              <div class="p-3 rounded-3 bg-light h-100">
                <div class="small compare-muted">Products</div>
                <div class="fw-semibold">${productCount}</div>
              </div>
            </div>
          </div>
          <div class="mb-3">
            <div class="small compare-muted fw-semibold mb-2">Domains</div>
            ${renderChipList(Array.from(domains).sort((a, b) => a.localeCompare(b)), 'No domains recorded.')}
          </div>
          <div class="mb-0">
            <div class="small compare-muted fw-semibold mb-2">Original sources</div>
            ${renderChipList(Array.from(originalSources).sort((a, b) => a.localeCompare(b)), 'No original sources recorded.', getSourceUrl)}
          </div>
          <div class="mt-3 small">${homepageUrl}</div>
        </div>
      </div>
    `;
  }

  function renderPairComparison(leftResource, rightResource) {
    const comparison = compareResources(leftResource, rightResource);
    const scoreClass = comparison.similarityScore >= 60 ? 'text-success' : comparison.similarityScore >= 25 ? 'text-warning' : 'text-danger';

    const sharedDomains = renderChipList(comparison.sharedDomains, 'No shared domains.');
    const sharedSources = renderChipList(comparison.sharedOriginalSources, 'No shared original sources.', getSourceUrl);
    const sharedCategoryLabel = comparison.sharedCategory ? categoryLabel(comparison.sharedCategory) : 'Different categories';

    return `
      <div class="card compare-card shadow-sm mb-4">
        <div class="card-body p-4">
          <div class="row g-4 align-items-stretch mb-3">
            <div class="col-lg-5">
              ${renderResourceCard(leftResource)}
            </div>
            <div class="col-lg-2 d-flex align-items-center justify-content-center">
              <div class="text-center p-3">
                <div class="small text-uppercase compare-muted fw-semibold mb-2">Similarity</div>
                <div class="compare-score ${scoreClass}">${comparison.similarityScore.toFixed(1)}</div>
                <div class="compare-muted mt-2">${comparison.sharedFeatureCount} shared feature${comparison.sharedFeatureCount === 1 ? '' : 's'}</div>
                <div class="mt-2"><i class="bi bi-${categoryIcon(comparison.sharedCategory || leftResource.category)}"></i> ${escapeHtml(sharedCategoryLabel)}</div>
              </div>
            </div>
            <div class="col-lg-5">
              ${renderResourceCard(rightResource)}
            </div>
          </div>

          <div class="row g-3">
            <div class="col-md-6">
              <div class="p-3 rounded-3 bg-light h-100">
                <div class="fw-semibold mb-2">Shared domains</div>
                ${sharedDomains}
              </div>
            </div>
            <div class="col-md-6">
              <div class="p-3 rounded-3 bg-light h-100">
                <div class="fw-semibold mb-2">Shared original sources</div>
                ${sharedSources}
              </div>
            </div>
          </div>
        </div>
      </div>
    `;
  }

  function renderTopMatches(resource) {
    const matches = state.resources
      .filter(candidate => candidate.id && candidate.id !== resource.id)
      .map(candidate => {
        const comparison = compareResources(resource, candidate);
        return { candidate, comparison };
      })
      .filter(result => result.comparison.sharedFeatureCount > 0)
      .sort((left, right) => {
        if (right.comparison.similarityScore !== left.comparison.similarityScore) {
          return right.comparison.similarityScore - left.comparison.similarityScore;
        }
        if (right.comparison.sharedFeatureCount !== left.comparison.sharedFeatureCount) {
          return right.comparison.sharedFeatureCount - left.comparison.sharedFeatureCount;
        }
        return left.candidate.id.localeCompare(right.candidate.id);
      })
      .slice(0, 15);

    if (!matches.length) {
      return `
        <div class="compare-empty">
          <h3 class="h5 mb-2">No overlaps found</h3>
          <p class="mb-0">This resource does not currently share domains or original sources with any other indexed resource.</p>
        </div>
      `;
    }

    return `
      <div class="card compare-card shadow-sm">
        <div class="card-body p-4">
          <div class="d-flex justify-content-between flex-wrap gap-2 align-items-center mb-3">
            <div>
              <h2 class="h4 mb-1">Closest matches</h2>
              <div class="compare-muted">Sorted by weighted overlap of category, domains, and original sources.</div>
            </div>
            <div class="compare-muted small">Top ${matches.length} of ${Math.max(state.resources.length - 1, 0)}</div>
          </div>

          <div class="table-responsive">
            <table class="table table-hover align-middle compare-table mb-0">
              <thead>
                <tr>
                  <th>Category</th>
                  <th>Resource</th>
                  <th>Similarity</th>
                  <th>Shared domains</th>
                  <th>Shared original sources</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                ${matches.map(({ candidate, comparison }) => `
                  <tr>
                    <td>
                      <div class="d-flex align-items-center gap-2">
                        <i class="bi bi-${categoryIcon(candidate.category)}"></i>
                        <span>${escapeHtml(categoryLabel(candidate.category))}</span>
                      </div>
                    </td>
                    <td>
                      <div class="fw-semibold">${escapeHtml(candidate.name || candidate.id)}</div>
                      <div class="small text-muted font-monospace">${escapeHtml(candidate.id)}</div>
                    </td>
                    <td>
                      <span class="badge text-bg-primary">${comparison.similarityScore.toFixed(1)}</span>
                    </td>
                    <td>${comparison.sharedDomains.length}</td>
                    <td>${comparison.sharedOriginalSources.length}</td>
                    <td class="text-end">
                      <a class="btn btn-outline-secondary btn-sm" href="${registryPath(`/compare/?resource=${encodeURIComponent(resource.id)}&compare=${encodeURIComponent(candidate.id)}`)}">Open pair</a>
                    </td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    `;
  }

  function renderMessage(message, type = 'info') {
    const container = document.getElementById('comparison-message');
    if (!container) return;

    if (!message) {
      container.innerHTML = '';
      return;
    }

    const alertClass = type === 'danger' ? 'alert-danger' : type === 'warning' ? 'alert-warning' : 'alert-info';
    container.innerHTML = `<div class="alert ${alertClass} mb-0">${escapeHtml(message)}</div>`;
  }

  function getSelectedResources() {
    const primaryInput = document.getElementById('resource-id');
    const compareInput = document.getElementById('compare-id');
    return {
      primaryValue: primaryInput ? primaryInput.value.trim() : '',
      compareValue: compareInput ? compareInput.value.trim() : ''
    };
  }

  function resolveResource(value) {
    const normalized = normalize(value);
    if (!normalized) return null;

    const exactId = state.resources.find(resource => normalize(resource.id) === normalized);
    if (exactId) return exactId;

    const exactName = state.resources.find(resource => normalize(resource.name) === normalized);
    if (exactName) return exactName;

    const idMatches = state.resources.filter(resource => normalize(resource.id).includes(normalized));
    if (idMatches.length === 1) return idMatches[0];

    const nameMatches = state.resources.filter(resource => normalize(resource.name).includes(normalized));
    if (nameMatches.length === 1) return nameMatches[0];

    return null;
  }

  function populateResourceLists() {
    const dataListIds = ['resource-id-list', 'compare-id-list'];
    const sortedResources = [...state.resources].sort((left, right) => {
      const leftLabel = (left.name || left.id || '').toLowerCase();
      const rightLabel = (right.name || right.id || '').toLowerCase();
      return leftLabel.localeCompare(rightLabel);
    });

    dataListIds.forEach(listId => {
      const list = document.getElementById(listId);
      if (!list) return;
      list.innerHTML = '';

      sortedResources.forEach(resource => {
        if (!resource.id) return;
        const option = document.createElement('option');
        option.value = resource.id;
        option.label = formatResourceLabel(resource);
        list.appendChild(option);
      });
    });
  }

  function applyQueryToForm() {
    const params = new URLSearchParams(window.location.search);
    const primaryInput = document.getElementById('resource-id');
    const compareInput = document.getElementById('compare-id');

    if (primaryInput && params.get('resource')) {
      primaryInput.value = params.get('resource');
    }
    if (compareInput && params.get('compare')) {
      compareInput.value = params.get('compare');
    }
  }

  function updateQueryFromForm() {
    const { primaryValue, compareValue } = getSelectedResources();
    const url = new URL(window.location.href);

    if (primaryValue) {
      url.searchParams.set('resource', primaryValue);
    } else {
      url.searchParams.delete('resource');
    }

    if (compareValue) {
      url.searchParams.set('compare', compareValue);
    } else {
      url.searchParams.delete('compare');
    }

    window.history.replaceState({}, '', url);
  }

  function renderComparison() {
    const output = document.getElementById('comparison-output');
    if (!output) return;

    const { primaryValue, compareValue } = getSelectedResources();
    const primaryResource = resolveResource(primaryValue);
    const compareResource = resolveResource(compareValue);

    if (!primaryValue) {
      renderMessage('Enter a primary resource ID to start comparing.', 'info');
      output.innerHTML = `
        <div class="compare-empty">
          <h2 class="h4 mb-2">Choose a resource</h2>
          <p class="mb-0">Use the form above to load one resource or a pair of resources. The page will score overlap using shared domains and shared original sources.</p>
        </div>
      `;
      return;
    }

    if (!primaryResource) {
      renderMessage(`No KG-Registry resource matched "${primaryValue}".`, 'danger');
      output.innerHTML = '';
      return;
    }

    if (compareValue && !compareResource) {
      renderMessage(`No KG-Registry resource matched "${compareValue}".`, 'danger');
      output.innerHTML = '';
      return;
    }

    if (compareValue && compareResource) {
      renderMessage(`Comparing ${primaryResource.id} with ${compareResource.id}.`, 'info');
      output.innerHTML = renderPairComparison(primaryResource, compareResource);
      return;
    }

    renderMessage(`Showing the strongest overlaps for ${primaryResource.id}.`, 'info');
    output.innerHTML = `
      <div class="mb-4">
        ${renderResourceCard(primaryResource)}
      </div>
      ${renderTopMatches(primaryResource)}
    `;
  }

  async function loadData() {
    const response = await fetch(registryPath('/registry/kgs.yml'));
    const text = await response.text();
    const data = jsyaml.load(text) || {};
    return Array.isArray(data.resources) ? data.resources : [];
  }

  async function initialize() {
    const form = document.getElementById('compare-form');
    if (!form) return;

    try {
      state.resources = await loadData();
      state.resourceMap = new Map(state.resources.filter(resource => resource && resource.id).map(resource => [resource.id, resource]));
      populateResourceLists();
      applyQueryToForm();
      renderComparison();
    } catch (error) {
      console.error('Failed to load registry data', error);
      renderMessage('Unable to load registry data for comparisons.', 'danger');
      const output = document.getElementById('comparison-output');
      if (output) {
        output.innerHTML = '';
      }
    }

    form.addEventListener('submit', event => {
      event.preventDefault();
      updateQueryFromForm();
      renderComparison();
    });

    const swapButton = document.getElementById('swap-inputs');
    if (swapButton) {
      swapButton.addEventListener('click', () => {
        const primaryInput = document.getElementById('resource-id');
        const compareInput = document.getElementById('compare-id');
        if (!primaryInput || !compareInput) return;

        const primaryValue = primaryInput.value;
        primaryInput.value = compareInput.value;
        compareInput.value = primaryValue;
        updateQueryFromForm();
        renderComparison();
      });
    }
  }

  document.addEventListener('DOMContentLoaded', initialize);
})();