---
layout: default
title: Compare Resources
description: Compare KG-Registry resources by shared domains and shared original sources.
permalink: /compare/
---

<style>
  .compare-hero {
    background: linear-gradient(135deg, rgba(13, 110, 253, 0.10), rgba(32, 201, 151, 0.10));
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 1.25rem;
  }

  .compare-hero-badge {
    background: rgba(13, 110, 253, 0.08);
    color: #0b5ed7;
    border-radius: 999px;
    padding: 0.5rem 0.9rem;
    font-weight: 600;
    white-space: nowrap;
  }

  .compare-score {
    font-size: 2.1rem;
    font-weight: 700;
    line-height: 1;
  }

  .compare-chip-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .compare-chip {
    border-radius: 999px;
    padding: 0.35rem 0.7rem;
    background: #f1f5f9;
    border: 1px solid #dbe2ea;
    font-size: 0.92rem;
  }

  .compare-card {
    border-radius: 1rem;
  }

  .compare-muted {
    color: #667085;
  }

  .compare-table thead th {
    white-space: nowrap;
  }

  .compare-empty {
    border: 1px dashed rgba(0, 0, 0, 0.2);
    border-radius: 1rem;
    padding: 1.5rem;
    background: rgba(255, 255, 255, 0.7);
  }

  .compare-field-label {
    min-height: 2rem;
    display: flex;
    align-items: end;
  }

  .compare-field-subtitle {
    min-height: 2.5rem;
  }

  @media (max-width: 991.98px) {
    .compare-field-label,
    .compare-field-subtitle {
      min-height: 0;
    }
  }
</style>

<div class="compare-hero mb-4">
  <div class="p-4 p-lg-5">
    <div class="d-flex flex-column flex-lg-row justify-content-between gap-3 align-items-start align-items-lg-center">
      <div>
        <div class="text-uppercase fw-semibold small compare-muted mb-2">Resource similarity</div>
        <h1 class="mb-2">Compare KG-Registry Resources</h1>
        <p class="lead mb-0" style="max-width: 54rem;">
          Compare one resource against the registry or compare a specific pair by the features they share:
          category, domains, and original sources.
        </p>
      </div>
    </div>
  </div>
</div>

<div class="card compare-card shadow-sm mb-4">
  <div class="card-body p-4">
    <form id="compare-form" class="row g-3 align-items-end">
      <div class="col-lg-5">
        <label for="resource-id" class="form-label fw-semibold compare-field-label">Primary resource ID</label>
        <input id="resource-id" name="resource" class="form-control form-control-lg" list="resource-id-list" placeholder="e.g. raras" autocomplete="off" spellcheck="false" />
        <datalist id="resource-id-list"></datalist>
        <div class="form-text compare-field-subtitle">Enter a KG-Registry resource ID or resource name.</div>
      </div>
      <div class="col-lg-5">
        <label for="compare-id" class="form-label fw-semibold compare-field-label">Second resource ID</label>
        <input id="compare-id" name="compare" class="form-control form-control-lg" list="compare-id-list" placeholder="Leave blank to compare against the registry" autocomplete="off" spellcheck="false" />
        <datalist id="compare-id-list"></datalist>
        <div class="form-text compare-field-subtitle">Optional. If provided, the page compares only those two resources.</div>
      </div>
      <div class="col-lg-2 d-grid gap-2">
        <button class="btn btn-primary btn-lg" type="submit">
          <i class="bi bi-search me-1"></i>Compare
        </button>
        <button class="btn btn-outline-secondary" type="button" id="swap-inputs">
          <i class="bi bi-arrow-left-right me-1"></i>Swap
        </button>
      </div>
    </form>
  </div>
</div>

<div id="comparison-message" class="mb-4"></div>
<div id="comparison-output"></div>

<script>
  window.kgRegistryBaseUrl = {{ site.baseurl | jsonify }};
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js"></script>
<script src="{{ '/assets/js/resource-compare.js' | relative_url }}"></script>