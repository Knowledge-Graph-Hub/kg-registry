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
        "GraphProduct": "globe",
        "Product": "box",
        "MappingProduct": "map",
        "ProcessProduct": "gear",
        "DataModelProduct": "diagram-3",
        "GraphicalInterface": "window",
        "ProgrammingInterface": "code-square"
    };

    // Cache frequently accessed DOM elements
    const $tableDiv = $("#tableDiv");
    const $tableMain = $('#table-main');
    const $searchVal = $("#searchVal");
    const $ddDomains = $("#dd-domains");
    const $ddResourceTypes = $("#dd-resourcetypes");
    const $ddCollections = $("#dd-collections");
    const $resourceCount = $("#resource-count");

    // Update resource count display
    function updateResourceCount(count, totalCount) {
        if (count === totalCount) {
            $resourceCount.text(count + " resources");
        } else {
            $resourceCount.text(count + " of " + totalCount + " resources");
        }
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
                <table id="ont_table" class="table table-hover sortable">
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
                                <span>Evaluation</span>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        ${content}
                    </tbody>
                </table>
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

        return `
            <tr class="${is_inactive}">
                <th scope="row" style="vertical-align: middle;">
                    <a href="resource/${id}/${id}.html">
                        ${id}
                    </a>
                </th>
                <td style="vertical-align: middle;">
                    ${title}
                </td>
                <td style="vertical-align: middle;">
                    <span style="background-color: #ff8d82">${is_obsolete}</span>
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
        return evalUrl ?
            `<a role="button" class="btn btn-outline-primary" href="${evalUrl}" aria-label="View evaluation for ${id}" title="Evaluation">
                <i class="bi-clipboard-check" aria-hidden="true"></i>
            </a>` : '';
    }

    // Lazily initialize sortable tables
    function initSortableTables() {
        const sortableTables = document.querySelectorAll('table.sortable');
        for (let i = 0; i < sortableTables.length; i++) {
            new SortableTable(sortableTables[i]);
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
     * Optimize renderTable function for faster rendering by:
     * 1. Splitting rendering into chunks for large datasets
     * 2. Using document fragments for DOM operations
     * 3. Loading dashboard data asynchronously in parallel
     */
    function renderTable(data) {
        // Show loading indicator right away
        $tableDiv.html('<div class="loading-indicator">Loading resources...</div>');

        // Initialize total resource count
        let totalCount = 0;
        if (data && Array.isArray(data)) {
            totalCount = data.length;
        }

        // Check if data is valid before processing
        if (!data || !Array.isArray(data) || data.length === 0) {
            $tableDiv.html('<div class="alert alert-info">No resources found - please try another search.</div>');
            $tableMain.css('display', 'block');
            updateResourceCount(0, totalCount);
            return;
        }

        // Update resource count immediately
        updateResourceCount(totalCount, totalCount);

        // Preprocess data before manipulation
        const processedData = data.map(item => {
            const id = item.id || '';
            const is_inactive = item.activity_status === "inactive" || item.activity_status === "orphaned" ? "inactive_row" : "";
            const is_obsolete = item.is_obsolete ? "(obsolete)" :
                (item.activity_status === "inactive" || item.activity_status === "orphaned") ?
                    `(${item.activity_status})` : "";

            // Pre-compute domain for faster sorting
            const domainValues = Array.isArray(item.domains) ?
                item.domains.map(d => d.trim()) :
                Array.isArray(item.domain) ? // Backward compatibility
                    item.domain.map(d => d.trim()) :
                    [(item.domains ? item.domains.trim() :
                        item.domain ? item.domain.trim() : "Unknown")];

            return {
                item,
                id,
                is_inactive,
                is_obsolete,
                domainValues,
                domainValue: domainValues[0] // Keep for backward compatibility
            };
        });

        // Separate dashboard data fetch from the rendering
        setTimeout(() => {
            renderBasicTable(processedData);
        }, 0);

        // If dashboard data should be loaded, do it asynchronously
        if (typeof shouldFetchDashboardData !== 'undefined' && shouldFetchDashboardData) {
            setTimeout(() => {
                fetchAndProcessDashboardData(data);
            }, 50);
        }
    }

    // Render the basic table structure without waiting for dashboard data
    function renderBasicTable(processedData) {
        // Check data again before processing
        if (!processedData || !Array.isArray(processedData) || processedData.length === 0) {
            $tableDiv.html('<div class="alert alert-info">No resources found matching your criteria.</div>');
            $tableMain.css('display', 'block');
            updateResourceCount(0, window.totalResourceCount || 0);
            return;
        }

        // Update the count with filtered data length
        updateResourceCount(processedData.length, window.totalResourceCount || processedData.length);

    let table = '';

        // Process in chunks for large datasets (improves responsiveness)
        const CHUNK_SIZE = 50;
        const processChunk = (startIndex) => {
            const endIndex = Math.min(startIndex + CHUNK_SIZE, processedData.length);

            for (let i = startIndex; i < endIndex; i++) {
                const item = processedData[i];
                // Skip undefined items
                if (!item) continue;

                const { item: originalItem, id, is_inactive, is_obsolete, domainValues } = item;
                const template = createTableRow(originalItem, id, is_inactive, is_obsolete);

                // Always render as a flat list (no grouping)
                table += template;
            }

            // If more chunks to process, schedule next chunk
            if (endIndex < processedData.length) {
                setTimeout(() => processChunk(endIndex), 0);
            } else {
                finishRendering();
            }
        };

        // Handle completion of all chunks
        const finishRendering = () => {
            if (table.length === 0) {
                $tableDiv.html('<div class="alert alert-info">No resources found matching your criteria.</div>');
            } else {
                $tableDiv.html(tableHtml(table, false, ""));
            }

            // Initialize sortable tables after content is added
            initSortableTables();

            // Show the main table
            $tableMain.css('display', 'block');
        };

        // Start processing the first chunk
        processChunk(0);
    }

    // Get dashboard data in the background
    function fetchAndProcessDashboardData(data) {
        const dashboard_url = "https://raw.githubusercontent.com/OBOFoundry/obo-dash.github.io/gh-pages/dashboard/dashboard-results.json";

        fetch(dashboard_url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(dashboard_data => {
                // Process dashboard data
                updateTablesWithDashboardData(data, dashboard_data);
            })
            .catch(error => {
                console.error('Error fetching dashboard data:', error);
            });
    }

    // Update tables with dashboard data without re-rendering everything
    function updateTablesWithDashboardData(data, dashboard_data) {
        // Implementation would go here
    }

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
        const selectedDomain = $ddDomains.children("option:selected").val();
        const selectedResourceType = $ddResourceTypes.children("option:selected").val();
        const selectedCollection = $ddCollections.children("option:selected").val();

        // Check for empty data to avoid errors
        if (!data || !data.resources) return;

    // Store total count for reference in updating resource count
    window.totalResourceCount = data.resources.length;

        // Filter in steps for better performance
        let filteredData = data.resources.filter(x => x.category !== undefined);

        // Exclude entries with domain 'stub' from the main page listing at all times
        filteredData = filteredData.filter(x => {
            // Handle multi-valued domains and legacy field
            const domains = Array.isArray(x.domains) ? x.domains : (Array.isArray(x.domain) ? x.domain : (x.domains || x.domain ? [x.domains || x.domain] : []));
            return !domains.some(d => (d || '').toLowerCase() === 'stub');
        });

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

    // Helper function to populate dropdowns
    function populateDropdown(selector, items, emptyOption = true, formatFunction = null) {
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

            fragment.appendChild(option);
        });

        dropdown[0].appendChild(fragment);
    }

    // Run search initialization
    search();

    // Load data with a single fetch
    fetch('registry/kgs.jsonld')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then((data) => {
            // Show table container immediately
            $tableMain.css('display', 'block');
            
            // Store total count and update display
            window.totalResourceCount = data.resources.length;
            updateResourceCount(data.resources.length, data.resources.length);

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

            // Populate collections dropdown with capitalized entries
            populateDropdown("#dd-collections", collections, true, capitalize);
            $("#dd-collections option[value='']").text('All Collections');

            // Defer initial render to the first filter cycle to apply default rules (flat list, no 'stub')

            // Set up event handlers with debounce
            const filterHandler = debounce(() => apply_all_filters(data), 100);

            $ddDomains.on("change", filterHandler);
            $ddResourceTypes.on("change", filterHandler);
            $ddCollections.on("change", filterHandler);
            $searchVal.on("keyup", filterHandler);

            // Create observer for table sorting
            const observer = new MutationObserver(function () {
                initSortableTables();
            });

            observer.observe($tableDiv[0], {
                childList: true,
                subtree: true
            });

            // Trigger initial filter to apply default exclusions
            filterHandler();
        })
        .catch(error => {
            console.error('Error loading data:', error);
            $tableDiv.html('<div class="alert alert-danger">Failed to load data. Please try refreshing the page.</div>');
            updateResourceCount(0, 0);
        });
});
