/*
Custom JS for KG-Registry
*/

jQuery(document).ready(function () {
    // Define debounce at the top for earlier availability
    function debounce(func, timeout = 300) {
        let timer;
        return (...args) => {
            clearTimeout(timer);
            timer = setTimeout(() => {
                func.apply(this, args);
            }, timeout);
        };
    }

    // Category to icon mapping (matches resource_detail.html)
    const categoryIcons = {
        "Aggregator": "grid-3x3",
        "Resource": "archive",
        "KnowledgeGraph": "globe",
        "DataSource": "shop",
        "DataModel": "diagram-3",
        "Ontology": "diagram-2",
        "GraphProduct": "globe",
        "Product": "box",
        "MappingProduct": "map",
        "ProcessProduct": "gear",
        "DataModelProduct": "diagram-3",
        "OntologyProduct": "diagram-2",
        "GraphicalInterface": "window",
        "ProgrammingInterface": "code-square"
    };

    // Collection metadata: display names and descriptions
    const collectionMetadata = {
        "aop": {
            displayName: "AOP",
            description: "This entity incorporates the Adverse Outcome Pathways (AOP) framework in some manner."
        },
        "ber": {
            displayName: "BER",
            description: "A resource or product relevant to the US Department of Energy Biological and Environmental Research (BER) program."
        },
        "omop": {
            displayName: "OMOP",
            description: "This entity is part of the OMOP Common Data Model ecosystem, including vocabularies and related standards used in OHDSI workflows."
        },
        "translator": {
            displayName: "Translator",
            description: "This entity is part of those developed and used by the NCATS Biomedical Translator program."
        },
        "obo-foundry": {
            displayName: "OBO Foundry",
            description: "This entity is an ontology from the OBO Foundry, a collaborative effort to create reference ontologies in the biomedical domain."
        },
        "okn": {
            displayName: "OKN",
            description: "This entity is part of the Prototype Open Knowledge Network (OKN), a knowledge graph network supported by the National Science Foundation (NSF)."
        }
    };

    // Cache frequently accessed DOM elements
    const $tableDiv = $("#tableDiv");
    const $searchVal = $("#searchVal");
    const $ddDomains = $("#dd-domains");
    const $ddResourceTypes = $("#dd-resourcetypes");
    const $ddCollections = $("#dd-collections");
    const $ddActivity = $("#dd-activity");
    const $ddEvaluation = $("#dd-evaluation");
    const $ddTaxa = $("#dd-taxa");
    const $resourceCount = $("#resource-count");
    const $kgCount = $("#kg-count");
    const $collectionDescContainer = $("#collection-description-container");
    const $collectionDescText = $("#collection-description-text");

    // Taxon hierarchy mapping loaded from generated YAML file
    let taxonHierarchyMap = {};

    // Warn once if the taxon filter can only match exact taxa
    function warnTaxonHierarchyUnavailable() {
        showRegistryWarning(
            'The organism/taxon hierarchy could not be loaded, so the Organism/Taxon ' +
            'filter will only match resources annotated with the exact taxon selected ' +
            '(not its descendants). All other filters are unaffected.'
        );
    }

    // Load taxon hierarchy mapping from YAML file
    fetch('registry/taxon_mapping.yaml')
        .then(response => {
            if (!response.ok) {
                console.warn('Failed to load taxon mapping YAML:', response.status, response.statusText);
                warnTaxonHierarchyUnavailable();
                return '';
            }
            return response.text();
        })
        .then(yamlText => {
            if (!yamlText) {
                return;
            }

            // Simple YAML parser for taxon_mapping.yaml
            // Expected format: taxon_hierarchy: { NCBITaxon:XXXXX: [list of taxa] }
            try {
                const lines = yamlText.trim().split('\n');
                let currentTaxon = null;

                for (let i = 0; i < lines.length; i++) {
                    const line = lines[i];
                    const trimmedLine = line.trim();

                    // Skip empty lines and the header
                    if (!trimmedLine || trimmedLine.startsWith('#') || trimmedLine === 'taxon_hierarchy:') {
                        continue;
                    }

                    // Check if this is a taxon key (starts with NCBITaxon: and ends with :)
                    // Look for pattern: "  NCBITaxon:XXXXX:"
                    if (trimmedLine.match(/^NCBITaxon:\d+:$/)) {
                        // Extract taxon ID (remove trailing colon)
                        currentTaxon = trimmedLine.slice(0, -1); // Remove the trailing ':'
                        taxonHierarchyMap[currentTaxon] = [];
                    } else if (currentTaxon && trimmedLine.startsWith('- NCBITaxon:')) {
                        // This is an item in the taxon list
                        const taxon = trimmedLine.substring(2).trim(); // Remove "- "
                        taxonHierarchyMap[currentTaxon].push(taxon);
                    } else if (currentTaxon && trimmedLine === '[]') {
                        // Empty list
                        taxonHierarchyMap[currentTaxon] = [];
                    }
                }

                console.log('Taxon hierarchy mapping loaded successfully with', Object.keys(taxonHierarchyMap).length, 'taxa');
            } catch (error) {
                console.error('Error parsing taxon mapping YAML:', error);
                warnTaxonHierarchyUnavailable();
            }
        })
        .catch(error => {
            console.error('Could not load taxon mapping file:', error);
            warnTaxonHierarchyUnavailable();
        });

    // Update resource count display
    function updateResourceCount(count, totalCount, kgCount, totalKgCount) {
        // Counts are only meaningful once data has loaded, so restore the
        // regular badge colors (they start out grey to signal "loading")
        $resourceCount.removeClass("bg-secondary bg-danger").addClass("bg-primary");
        $kgCount.removeClass("bg-secondary bg-danger").addClass("bg-success");

        if (count === totalCount) {
            $resourceCount.text(count + " resources");
        } else {
            $resourceCount.text(count + " of " + totalCount + " resources");
        }

        // Update KG count
        if (kgCount !== undefined) {
            if (kgCount === totalKgCount) {
                $kgCount.text(kgCount + " KGs");
            } else {
                $kgCount.text(kgCount + " of " + totalKgCount + " KGs");
            }
        }
    }

    // Put the counts into an explicit error state. A failed load must not look
    // like an empty registry ("0 resources") or like it is still loading.
    function setCountsError() {
        $resourceCount.removeClass("bg-secondary bg-primary").addClass("bg-danger")
            .text("— resources");
        $kgCount.removeClass("bg-secondary bg-success").addClass("bg-danger")
            .text("— KGs");
    }

    // Show a non-fatal warning (the table still works, but something degraded)
    function showRegistryWarning(message) {
        $("#registry-warning-container").html(
            `<div class="alert alert-warning alert-dismissible fade show mb-0" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>`
        );
    }

    function search() {
        // Cache selectors inside search for efficiency
        const $search = $('#search');
        const $searchResults = $('#search-results', $search);
        const $close = $('#close', $search);
        const $input = $('input', $search);
        $close.hide();
        var data = false;
        var matches = false;
        var find = function (phrase) {
            if (!data) {
                return $.ajax({
                    url: '/search.json',
                    dataType: 'json',
                    // Use cache option to enable browser caching
                    cache: true,
                    success: function (resp) {
                        // Create a document fragment for better performance
                        data = resp
                            .filter(p => p != null)
                            .map(function (p) {
                                // Pre-compute and store the words for faster searching
                                p.words = (p.title.toLowerCase() + ' ' + p.summary.toLowerCase()).match(/(\w+)/g) || [];
                                return p;
                            });
                        find(phrase);
                    }
                });
            }

            // Optimize filtering with early returns
            matches = data.filter(function (p) {
                // Skip processing if words array is empty
                if (!p.words || !p.words.length) return false;

                return phrase.filter(function (a) {
                    return p.words.some(function (b) {
                        return a === b || b.indexOf(a) === 0;
                    });
                }).length === phrase.length;
            });

            // Use document fragment for better DOM performance
            const fragment = document.createDocumentFragment();
            $(matches).each(function () {
                const li = document.createElement('li');
                li.innerHTML = '<h6>' + this.title + '</h6><p>' + this.title + '... <small><a href="' + this.url + '">Read more</a></small></p><hr>';
                fragment.appendChild(li);
            });

            $searchResults.append(fragment);
            $searchResults.show();
            $close.show();
        };

        function handleSearch() {
            $searchResults.empty();
            $searchResults.hide();
            $close.hide();

            var phrase = $input.val();
            if (phrase.length >= 4) {
                const words = phrase.toLowerCase().match(/(\w+)/g);
                if (words && words.length) {
                    find(words);
                }
            }
            return false;
        }

        // Use a single delegated event handler for input events
        $search.on('keyup focus', 'input', debounce(handleSearch, 100));

        $close.on('click', function () {
            $searchResults.hide();
            $close.hide();
            return false;
        });
    };

    // Set the first character of string to uppercase
    function capitalize(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    // Surround data table rows generated in renderTable function with table head
    function tableHtml(content, domain = false, tableDomains) {
        const header = domain ? `<div class="p-1 bg-light"><strong>${capitalize(tableDomains)}</strong></div>` : '';
        return `${header}
                <div class="registry-table-wrapper">
                <table id="ont_table" class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col" style="width: 15%; vertical-align: middle;">
                                <span class="sort-button" title="Sort by ID" data-sort="id" >
                                    ID <i class="bi-chevron-up" aria-hidden="true"></i>
                                </span>
                            </th>
                            <th scope="col" style="width: 15%; vertical-align: middle;">
                                <span class="sort-button" title="Sort by name" data-sort="name" >
                                    Name <i class="bi-chevron-up" aria-hidden="true"></i>
                                </span>
                            </th>
                            <th scope="col" style="width: 30%; vertical-align: middle;">
                                <span>Description</span>
                            </th>
                            <th scope="col" style="width: 5%; vertical-align: middle;" class="text-center">
                                <span title="Category Icon"></span>
                            </th>
                            <th scope="col" style="width: 15%; vertical-align: middle;">
                                <span>Resource Type</span>
                            </th>
                            <th scope="col" style="width: 10%; vertical-align: middle;">
                                <span>Quick Access</span>
                            </th>
                            <th scope="col" style="width: 10%; vertical-align: middle;">
                                <span class="sort-button" title="Sort by status" data-sort="license" >
                                    License <i class="bi-chevron-up" aria-hidden="true"></i>
                                </span>
                            </th>
                            <th scope="col" style="width: 5%; vertical-align: middle;" class="text-center">
                                <span>Eval</span>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        ${content}
                    </tbody>
                </table>
                </div>
                `;
    }

    // Helper function to create table row
    function createTableRow(item, id, is_inactive, is_obsolete) {
        // Extract values with defaults for speed
        const title = item.name || '';
        const description = item.description ?
            (item.description.toString().length > 140 ?
                item.description.toString().slice(0, 140).trim() + '...' :
                item.description) :
            '';
        const category = item.category || '';
        const resourcetype = category ?
            category.replace(/([a-z])([A-Z])/g, '$1 $2') :
            '';
        const homepage = item.homepage_url || '#';
        const license_box = createLicenseBox(item);

        // Get the icon for the category
        const iconName = categoryIcons[category] || 'box';

        // Warning badges suppressed on main listing (warnings still appear on detail pages)
        const warningBadge = '';

        // Build status badge for non-active resources
        let statusBadge = '';
        const status = (item.activity_status || '').toLowerCase();
        if (status && status !== 'active') {
            const tooltip = `Status: ${status}`.replace(/"/g, '&quot;');
            statusBadge = ` <span title="${tooltip}" style="cursor: help; text-decoration: underline dotted;">⏸</span>`;
        }

        return `
            <tr class="${is_inactive}">
                <th scope="row" style="vertical-align: middle;">
                    <a href="resource/${id}/${id}.html">
                        ${id}${warningBadge}${statusBadge}
                    </a>
                </th>
                <td style="vertical-align: middle;">
                    ${title}
                </td>
                <td style="vertical-align: middle;">
                    ${description}
                </td>
                <td class="text-center" style="vertical-align: middle;">
                    <i class="bi bi-${iconName}" style="font-size: 1.75em; color: #0d6efd;"></i>
                </td>
                <td style="vertical-align: middle;">
                    ${resourcetype}
                </td>
                <td style="vertical-align: middle;">
                    <div class="btn-group btn-group-sm" role="group">
                        <a class="btn btn-outline-primary" href="${homepage}" aria-label="Go to the homepage for ${title}" title="Go to the homepage for ${title}">
                            <i class="bi-house" aria-hidden="true"></i>
                        </a>
                        ${createPublicationButton(item, title)}
                    </div>
                </td>
                <td style="vertical-align: middle;">
                    ${license_box}
                </td>
                <td class="text-center" style="vertical-align: middle;">
                    ${createEvaluationButton(item, id)}
                </td>
            </tr>
        `;
    }

    // Helper functions to reduce CPU work in the main loop
    function createLicenseBox(item) {
        if (!item.license) return '';

        const license_url = item.license.id || '#';
        const license_logo = item.license.logo || '';
        const license_label = item.license.label || '';

        return license_logo ?
            `<a href="${license_url}"><img width="100px" src="${license_logo}" alt="${license_label}"/></a>` :
            `<a href="${license_url}">${license_label}</a>`;
    }

    // Helper function to normalize DOI by removing 'doi:' prefix if present
    function normalizeDoi(doi) {
        return doi ? doi.replace(/^doi:/, '') : doi;
    }

    function createPublicationButton(item, title) {
        return (item.publications && item.publications.length > 0) ?
            `<a role="button" class="btn btn-outline-primary" href="https://doi.org/${normalizeDoi(item.publications[0].id)}" aria-label="View the primary publication for ${title}" title="View the primary publication for ${title}">
                <i class="bi-book" aria-hidden="true"></i>
            </a>` :
            `<a role="button" class="btn btn-outline-primary disabled">
                <i class="bi-book" aria-hidden="true"></i>
            </a>`;
    }

    function createEvaluationButton(item, id) {
        const evalUrl = item.evaluation_page || '';

        if (!evalUrl) {
            return '';
        }

        // Check if this is an automated evaluation by looking at the URL
        const isAutomated = evalUrl.includes('_eval_automated');

        if (isAutomated) {
            return `<a role="button" class="btn btn-outline-info" href="${evalUrl}" aria-label="View automated evaluation for ${id}" title="Automated Evaluation (AI-Generated)">
                <i class="bi-robot" aria-hidden="true"></i>
            </a>`;
        } else {
            return `<a role="button" class="btn btn-outline-primary" href="${evalUrl}" aria-label="View manual evaluation for ${id}" title="Manual Evaluation (Curated)">
                <i class="bi-clipboard-check" aria-hidden="true"></i>
            </a>`;
        }
    }

    // constrain status values, make them sortable
    const DashboardStatus = {
        PASS: 5,  // all checks pass
        INFO: 4,  // info parameters returned
        WARN: 3,  // warnings raised
        ERROR: 2,  // errors raised
        FAILED: 1,  // dashboard QC failed to run
        UNKNOWN: 0,  // not found in dashboard results
    };

    /**
     * Rendering strategy: the filtered dataset is kept in memory and only a
     * batch of rows is put in the DOM at a time, with more appended as the user
     * scrolls. Building the row HTML string for ~1000 rows costs ~16ms, but
     * inserting them (~2MB of HTML, 8000+ cells) costs ~600ms and is paid again
     * on every filter change -- so the fix is to not create the nodes at all
     * until they are needed. See issue #662.
     *
     * Because only part of the table is in the DOM, sorting cannot be done by
     * reordering rows (what sorttable.js did); it sorts the dataset and
     * re-renders from the top.
     */
    const ROWS_PER_BATCH = 60;
    // How far below the viewport the sentinel is pulled in, in px. Larger means
    // rows are ready before the user reaches them, at the cost of more DOM.
    const SCROLL_PREFETCH_PX = 800;

    const renderState = {
        rows: [],          // the full filtered+sorted dataset
        rendered: 0,       // how many of those are currently in the DOM
        sortField: null,
        sortDir: 'ascending',
        observer: null,
    };

    // The value a row is sorted by, for each sortable column. Must mirror what
    // createTableRow actually displays in that column.
    function sortValue(item, field) {
        if (field === 'license') {
            return ((item.license && item.license.label) || '').toLowerCase();
        }
        return ((item && item[field]) || '').toString().toLowerCase();
    }

    function sortRows(rows) {
        if (!renderState.sortField) {
            return rows;
        }
        const field = renderState.sortField;
        const direction = renderState.sortDir === 'ascending' ? 1 : -1;
        // Sort a copy: the caller's array is the filter output, not ours to reorder.
        return rows.slice().sort((a, b) => {
            const av = sortValue(a, field);
            const bv = sortValue(b, field);
            if (av === bv) return 0;
            return av < bv ? -direction : direction;
        });
    }

    function rowHtml(item) {
        const id = item.id || '';
        const is_inactive = (item.activity_status === "inactive" || item.activity_status === "orphaned")
            ? "inactive_row" : "";
        const is_obsolete = item.is_obsolete ? "(obsolete)" :
            (item.activity_status === "inactive" || item.activity_status === "orphaned") ?
                `(${item.activity_status})` : "";
        return createTableRow(item, id, is_inactive, is_obsolete);
    }

    // Reflect the current sort on the freshly rendered header
    function applySortIndicators() {
        $tableDiv.find('#ont_table thead th').each(function () {
            const $th = $(this);
            const $button = $th.find('.sort-button');
            if (!$button.length) return;

            const $icon = $button.find('i');
            if ($button.data('sort') === renderState.sortField) {
                $th.attr('aria-sort', renderState.sortDir);
                $icon.attr('class', renderState.sortDir === 'ascending'
                    ? 'bi-chevron-up' : 'bi-chevron-down');
            } else {
                $th.removeAttr('aria-sort');
                $icon.attr('class', 'bi-chevron-up');
            }
        });
    }

    function updateSentinel() {
        const remaining = renderState.rows.length - renderState.rendered;
        const $sentinel = $('#table-sentinel');
        if (!$sentinel.length) return;

        if (remaining > 0) {
            $sentinel.html(
                `<div class="loading-indicator">
                    <div class="spinner-border spinner-border-sm text-primary me-2" aria-hidden="true"></div>
                    Loading ${remaining} more…
                </div>`
            );
        } else {
            // Everything is rendered; say so rather than leaving a dangling spinner
            $sentinel.html(renderState.rows.length
                ? `<div class="text-muted text-center py-2"><small>All ${renderState.rows.length} shown</small></div>`
                : '');
        }
    }

    function appendNextBatch() {
        const tbody = document.querySelector('#ont_table tbody');
        if (!tbody) return false;

        const start = renderState.rendered;
        const end = Math.min(start + ROWS_PER_BATCH, renderState.rows.length);
        if (start >= end) return false;

        let html = '';
        for (let i = start; i < end; i++) {
            html += rowHtml(renderState.rows[i]);
        }
        tbody.insertAdjacentHTML('beforeend', html);
        renderState.rendered = end;
        return true;
    }

    /**
     * Append batches until the sentinel is pushed below the prefetch line.
     * IntersectionObserver only fires on intersection *changes*, so if one batch
     * is too short to push the sentinel out of view it would never fire again
     * and loading would stall. This tops up until it does.
     */
    function fillViewport() {
        const sentinel = document.getElementById('table-sentinel');
        if (!sentinel) return;

        let guard = 0;
        while (renderState.rendered < renderState.rows.length && guard++ < 100) {
            if (sentinel.getBoundingClientRect().top > window.innerHeight + SCROLL_PREFETCH_PX) {
                break;
            }
            if (!appendNextBatch()) break;
        }
        updateSentinel();
    }

    function observeSentinel() {
        if (renderState.observer) {
            renderState.observer.disconnect();
        }
        const sentinel = document.getElementById('table-sentinel');
        if (!sentinel || typeof IntersectionObserver === 'undefined') {
            // No IntersectionObserver (or no sentinel): fall back to rendering
            // everything so the table is never silently truncated.
            while (appendNextBatch()) { /* keep going */ }
            updateSentinel();
            return;
        }

        renderState.observer = new IntersectionObserver(entries => {
            if (entries.some(entry => entry.isIntersecting)) {
                fillViewport();
            }
        }, { rootMargin: SCROLL_PREFETCH_PX + 'px' });

        renderState.observer.observe(sentinel);
    }

    /**
     * Render the filtered dataset.
     * @param {Array} data filtered resources
     */
    function renderTable(data) {
        if (!data || !Array.isArray(data) || data.length === 0) {
            if (renderState.observer) renderState.observer.disconnect();
            renderState.rows = [];
            renderState.rendered = 0;
            $tableDiv.html('<div class="alert alert-info">No resources found - please try another search.</div>');
            updateResourceCount(0, window.totalResourceCount || 0, 0, window.totalKgCount || 0);
            return;
        }

        const kgCount = data.filter(x => x.category && x.category.toLowerCase() === 'knowledgegraph').length;
        updateResourceCount(
            data.length, window.totalResourceCount || data.length,
            kgCount, window.totalKgCount || kgCount
        );

        renderState.rows = sortRows(data);
        renderState.rendered = 0;

        // Header + empty tbody; rows are appended in batches below.
        $tableDiv.html(tableHtml('', false, '') + '<div id="table-sentinel"></div>');
        applySortIndicators();
        fillViewport();
        observeSentinel();
    }

    // Re-render from the top with the current sort applied, reusing the
    // dataset already in memory (no refiltering needed).
    function resortAndRerender() {
        renderState.rows = sortRows(renderState.rows);
        renderState.rendered = 0;
        $('#ont_table tbody').empty();
        applySortIndicators();
        fillViewport();
        observeSentinel();
    }

    // Delegated so it survives the table being re-rendered
    $tableDiv.on('click', '.sort-button', function () {
        const field = $(this).data('sort');
        if (!field) return;

        if (renderState.sortField === field) {
            renderState.sortDir = renderState.sortDir === 'ascending' ? 'descending' : 'ascending';
        } else {
            renderState.sortField = field;
            renderState.sortDir = 'ascending';
        }
        resortAndRerender();
    });

    /**
     * Search the given fields {domain, description, id} for input text
     * @param {*} input input is a jQuery selector of the search box
     * @param {object} JsonData Ontology data to search through
     * @return {object} returns filtered json data
     */
    function Search(input, JsonData) {
        let value = input.val().toLowerCase();

        // Only search if term is at least 2 characters (better performance)
        if (value.length < 2) return JsonData;

        // Pre-compute the search term once
        const term = value;

        // Use faster filter with early returns
        return JsonData.filter((row) => {
            // Skip undefined values with defaults
            const id = (row.id || '').toLowerCase();
            const title = (row.title || '').toLowerCase();
            const description = (row.description || '').toLowerCase();

            // Handle domains as array or string
            let domainMatch = false;
            if (Array.isArray(row.domains)) {
                domainMatch = row.domains.some(d =>
                    (d || '').toLowerCase().includes(term)
                );
            } else if (Array.isArray(row.domain)) { // Backward compatibility
                domainMatch = row.domain.some(d =>
                    (d || '').toLowerCase().includes(term)
                );
            } else if (row.domains) {
                domainMatch = row.domains.toLowerCase().includes(term);
            } else if (row.domain) { // Backward compatibility
                domainMatch = row.domain.toLowerCase().includes(term);
            }

            // Check each field, return as soon as a match is found (faster)
            if (id.includes(term)) return true;
            if (domainMatch) return true;
            if (title.includes(term)) return true;
            if (description.includes(term)) return true;

            // No match found
            return false;
        });
    }

    /**
     * Applies filters taking into consideration the state of
     * all the other filters and search text
     * @param {object} data
     */
    function apply_all_filters(data) {
        // Get filter values once
        const selectedDomain = $ddDomains.find("option:selected").val();
        const selectedResourceType = $ddResourceTypes.find("option:selected").val();
        const selectedCollection = $ddCollections.find("option:selected").val();
        const selectedActivity = $ddActivity.find("option:selected").val();
        const selectedEvaluation = $ddEvaluation.find("option:selected").val();
        const selectedTaxon = $ddTaxa.find("option:selected").val();

        // Check for empty data to avoid errors
        if (!data || !data.resources) return;

        // Filter in steps for better performance
        let filteredData = data.resources.filter(x => x.category !== undefined);

        // Exclude entries with domain 'stub' from the main page listing at all times
        filteredData = filteredData.filter(x => {
            // Handle multi-valued domains and legacy field
            const domains = Array.isArray(x.domains) ? x.domains : (Array.isArray(x.domain) ? x.domain : (x.domains || x.domain ? [x.domains || x.domain] : []));
            return !domains.some(d => (d || '').toLowerCase() === 'stub');
        });

        // Store total count for reference in updating resource count (after excluding stub pages)
        window.totalResourceCount = filteredData.length;

        // Store total KG count
        window.totalKgCount = filteredData.filter(x => x.category && x.category.toLowerCase() === 'knowledgegraph').length;

        // Only apply filters if values are selected
        if (selectedResourceType) {
            filteredData = filteredData.filter(x => x.category && x.category.includes(selectedResourceType));
        }

        if (selectedDomain) {
            filteredData = filteredData.filter(x => {
                const domains = Array.isArray(x.domains) ? x.domains : (Array.isArray(x.domain) ? x.domain : (x.domains || x.domain ? [x.domains || x.domain] : []));
                const sel = selectedDomain.toLowerCase();
                return domains.some(d => (d || '').toLowerCase() === sel);
            });

            // Ensure uniqueness when domain filter is active (avoid duplicates across multiple domains)
            const seen = new Set();
            filteredData = filteredData.filter(x => {
                const key = x.id || x.name || JSON.stringify(x);
                if (seen.has(key)) return false;
                seen.add(key);
                return true;
            });
        }

        if (selectedCollection) {
            filteredData = filteredData.filter(x => {
                if (Array.isArray(x.collection)) {
                    return x.collection.some(c => c.includes(selectedCollection));
                }
                return x.collection && x.collection.includes(selectedCollection);
            });
        }

        // Apply activity status filter
        if (selectedActivity) {
            filteredData = filteredData.filter(x => {
                const activityStatus = (x.activity_status || 'active').toLowerCase();
                return activityStatus === selectedActivity.toLowerCase();
            });
        }

        // Apply evaluation filter
        if (selectedEvaluation) {
            filteredData = filteredData.filter(x => {
                const hasEvaluation = x.evaluation_page !== undefined && x.evaluation_page !== null;
                const isAutomated = hasEvaluation && x.evaluation_page.includes('_eval_automated');

                if (selectedEvaluation === 'yes') {
                    // With any evaluation (manual or automated)
                    return hasEvaluation;
                } else if (selectedEvaluation === 'manual') {
                    // With manual evaluation only
                    return hasEvaluation && !isAutomated;
                } else if (selectedEvaluation === 'automated') {
                    // With automated evaluation only
                    return isAutomated;
                } else if (selectedEvaluation === 'no') {
                    // Without any evaluation
                    return !hasEvaluation;
                }
                return true;
            });
        }

        // Apply taxon filter with hierarchical expansion
        if (selectedTaxon) {
            // Get the matching taxa from the hierarchy map (includes descendants)
            const matchingTaxa = taxonHierarchyMap[selectedTaxon] || [selectedTaxon];
            console.log('Applying taxon filter:', {
                selectedTaxon: selectedTaxon,
                hierarchyMapSize: Object.keys(taxonHierarchyMap).length,
                matchingTaxa: matchingTaxa,
                resourcesBeforeFilter: filteredData.length
            });
            filteredData = filteredData.filter(x => {
                if (Array.isArray(x.taxon)) {
                    return x.taxon.some(t => matchingTaxa.includes(t));
                }
                return x.taxon && matchingTaxa.includes(x.taxon);
            });
            console.log('Taxon filter result:', {
                resourcesAfterFilter: filteredData.length,
                matchingResources: filteredData.slice(0, 5).map(x => x.id)
            });
        }

        // Apply search filter
        filteredData = Search($searchVal, filteredData);

        // Always render a flat list (no group-by)
        renderTable(filteredData);
    }

    /**
     * Apply selected checkbox filter to data passed in
     * @param {object} data
     */
    // applyFilters is no longer needed since we always render a flat list

    /**
     * Sort json resource data by the given sort field
     * @param {Object} data
     * @param {string|number} sortField
     */
    function sortByField(data, sortField) {
        return data.sort(function (a, b) {
            // Handle domain/domains property name change
            if (sortField === "domain") {
                const aValue = a.domains || a.domain || "";
                const bValue = b.domains || b.domain || "";
                const aString = Array.isArray(aValue) ? aValue[0] || "" : aValue;
                const bString = Array.isArray(bValue) ? bValue[0] || "" : bValue;

                return aString.toLowerCase().localeCompare(bString.toLowerCase());
            }

            // Handle regular fields
            if (a[sortField] === undefined || b[sortField] === undefined) {
                return 0;
            }
            if (a[sortField].toLowerCase() < b[sortField].toLowerCase()) {
                return -1;
            }
            if (a[sortField].toLowerCase() > b[sortField].toLowerCase()) {
                return 1;
            }
            return 0;
        });
    }

    // Helper function to format resource type names from camelCase to space-separated words
    function formatResourceType(resourceType) {
        // Convert camelCase to space-separated words (e.g., "DataModel" to "Data Model")
        return resourceType.replace(/([a-z])([A-Z])/g, '$1 $2');
    }

    // Helper function to get collection display name from metadata
    function getCollectionDisplayName(collectionCode) {
        return collectionMetadata[collectionCode]?.displayName || capitalize(collectionCode);
    }

    // Helper function to update collection description display
    function updateCollectionDescription(collectionCode) {
        if (collectionCode && collectionMetadata[collectionCode]) {
            const metadata = collectionMetadata[collectionCode];
            const displayText = `Collection ${metadata.displayName} selected. ${metadata.description}`;
            $collectionDescText.text(displayText);
            $collectionDescContainer.show();
        } else {
            $collectionDescContainer.hide();
        }
    }

    // Helper function to populate dropdowns
    function populateDropdown(selector, items, emptyOption = true, formatFunction = null, metadata = null) {
        const dropdown = $(selector);
        dropdown.empty();

        if (emptyOption) {
            dropdown.append('<option value=""></option>');
        }

        // Use document fragment for better performance
        const fragment = document.createDocumentFragment();
        items.forEach(item => {
            const option = document.createElement('option');
            option.value = item; // Keep the original value for filtering

            // Apply formatting function if provided, otherwise use the item as is
            option.textContent = formatFunction ? formatFunction(item) : item;

            // Add title attribute from metadata if available
            if (metadata && metadata[item]) {
                option.title = metadata[item].description;
            }

            fragment.appendChild(option);
        });

        dropdown[0].appendChild(fragment);
    }

    // Run search initialization
    search();

    // The registry fetch is started by assets/js/registry-data.js, which loads
    // before jQuery so the request goes out in parallel with the CDN scripts
    // instead of waiting for them. See issue #662.
    function fetchRegistryData() {
        if (window.KGRegistryData) {
            return window.KGRegistryData.take();
        }
        // registry-data.js failed to load; surface that rather than silently
        // rendering an empty registry.
        return Promise.reject(new Error(
            'registry-data.js did not load, so the registry data was never requested'
        ));
    }

    // Show a clearly-distinct failure state. This must not be confusable with
    // "still loading" or "the registry is empty".
    function showLoadError(error) {
        console.error('Error loading data:', error);
        $tableDiv.html(
            `<div class="alert alert-danger" role="alert">
                <h5 class="alert-heading">
                    <i class="bi-exclamation-triangle-fill" aria-hidden="true"></i>
                    Could not load the registry data
                </h5>
                <p class="mb-2">
                    The registry table could not be displayed because the data failed to
                    load. This is a problem loading the page, not an empty registry.
                </p>
                <p class="mb-3"><small>Details: ${error && error.message ? error.message : error}</small></p>
                <button type="button" class="btn btn-outline-danger btn-sm" id="retry-load">
                    <i class="bi-arrow-clockwise" aria-hidden="true"></i> Retry
                </button>
            </div>`
        );
        setCountsError();
        $('#retry-load').on('click', loadRegistryData);
    }

    // The counterpart to showLoadError for the other failure mode: the data
    // arrived intact but an exception was thrown while rendering it. Retrying
    // is pointless here (a deterministic render bug fails identically every
    // time), so offer a link to the issue tracker instead. See issue #664.
    function showRenderError(error) {
        console.error('Error rendering data:', error);
        $tableDiv.html(
            `<div class="alert alert-danger" role="alert">
                <h5 class="alert-heading">
                    <i class="bi-exclamation-triangle-fill" aria-hidden="true"></i>
                    Could not display the registry data
                </h5>
                <p class="mb-2">
                    The registry data loaded, but an error occurred while
                    displaying it. This is a problem with the page or the data,
                    not with your connection, so retrying will not help.
                </p>
                <p class="mb-3"><small>Details: ${error && error.message ? error.message : error}</small></p>
                <a class="btn btn-outline-danger btn-sm"
                   href="https://github.com/Knowledge-Graph-Hub/kg-registry/issues"
                   target="_blank" rel="noopener">
                    <i class="bi-bug" aria-hidden="true"></i> Report this problem
                </a>
            </div>`
        );
        setCountsError();
    }

    function loadRegistryData() {
        $tableDiv.html(
            `<div class="loading-indicator" role="status" aria-live="polite">
                <div class="spinner-border spinner-border-sm text-primary me-2" aria-hidden="true"></div>
                Loading registry data…
            </div>`
        );

        // Keep the two failure modes distinct (issue #664): a rejected fetch
        // is a load failure, but an exception thrown by onRegistryDataLoaded
        // means the data arrived and only the rendering broke. The
        // two-argument then() ensures showLoadError never sees render errors.
        return fetchRegistryData().then(
            data => {
                try {
                    onRegistryDataLoaded(data);
                } catch (error) {
                    showRenderError(error);
                }
            },
            showLoadError
        );
    }

    function onRegistryDataLoaded(data) {
        if (!data || !Array.isArray(data.resources)) {
            throw new Error('Registry data is missing its list of resources');
        }

        console.log('Data loaded: total resources =', data.resources.length);

        // Calculate total count excluding stub pages
        const nonStubResources = data.resources.filter(r => {
            const domains = Array.isArray(r.domains) ? r.domains : (Array.isArray(r.domain) ? r.domain : (r.domains || r.domain ? [r.domains || r.domain] : []));
            return !domains.some(d => (d || '').toLowerCase() === 'stub');
        });

        // Store total count and update display
        window.totalResourceCount = nonStubResources.length;

        // Store total KG count
        window.totalKgCount = nonStubResources.filter(r => r.category && r.category.toLowerCase() === 'knowledgegraph').length;

        updateResourceCount(nonStubResources.length, nonStubResources.length, window.totalKgCount, window.totalKgCount);

        // Extract domains (handling multi-valued domains) and remove 'stub'
        let domains = [...new Set(
            data.resources
                .filter(r => r.domains !== undefined || r.domain !== undefined)
                .flatMap(r => {
                    // Handle both array and string values, and both property names
                    if (Array.isArray(r.domains)) {
                        return r.domains.map(d => d.trim());
                    } else if (Array.isArray(r.domain)) { // Backward compatibility
                        return r.domain.map(d => d.trim());
                    } else if (r.domains) {
                        return [r.domains.trim()];
                    } else if (r.domain) { // Backward compatibility
                        return [r.domain.trim()];
                    }
                    return ["Unknown"];
                })
        )]
            // Remove 'stub' (case-insensitive)
            .filter(d => (d || '').toLowerCase() !== 'stub');
        domains.sort();

        // Extract resource types (fix for duplication issue)
        const resourceTypes = [...new Set(
            data.resources
                .filter(r => r.category !== undefined)
                .map(r => r.category.trim())
        )];
        resourceTypes.sort();

        // Extract collections
        const collections = [...new Set(
            data.resources
                .filter(r => r.collection !== undefined)
                .flatMap(r => {
                    if (Array.isArray(r.collection)) {
                        return r.collection.map(c => c.trim());
                    }
                    return [r.collection.trim()];
                })
        )];
        collections.sort();

        // Populate dropdowns (avoids duplication)
        populateDropdown("#dd-domains", domains);
        $("#dd-domains option[value='']").text('All Domains');

        // Use the formatResourceType function for resource types dropdown
        populateDropdown("#dd-resourcetypes", resourceTypes, true, formatResourceType);
        $("#dd-resourcetypes option[value='']").text('All Resource Types');

        // Populate collections dropdown with capitalized entries and descriptions
        populateDropdown("#dd-collections", collections, true, getCollectionDisplayName, collectionMetadata);
        $("#dd-collections option[value='']").text('All Collections');

        // Defer initial render to the first filter cycle to apply default rules (flat list, no 'stub')

        // Set up event handlers with debounce
        const filterHandler = debounce(() => apply_all_filters(data), 100);

        $ddDomains.on("change", filterHandler);
        $ddResourceTypes.on("change", filterHandler);
        $ddCollections.on("change", function() {
            updateCollectionDescription($(this).val());
            filterHandler();
        });
        $ddActivity.on("change", filterHandler);
        $ddEvaluation.on("change", filterHandler);
        $ddTaxa.on("change", filterHandler);
        $searchVal.on("keyup", filterHandler);

        // Trigger initial filter to apply default exclusions
        filterHandler();
    }

    loadRegistryData();
});
