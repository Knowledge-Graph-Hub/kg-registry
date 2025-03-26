/*
Custom JS for KG-Registry
*/

jQuery(document).ready(function() {
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

    // Cache frequently accessed DOM elements
    const $tableDiv = $("#tableDiv");
    const $tableMain = $('#table-main');
    const $searchVal = $("#searchVal");
    const $ddDomains = $("#dd-domains");
    const $ddResourceTypes = $("#dd-resourcetypes");
    
    function search() {
        $('#close', search).hide();
        var data = false;
        var matches = false;
        var search = $('#search');
        var find = function(phrase) {
            if (!data) {
                return $.ajax({
                    url: '/search.json',
                    dataType: 'json',
                    // Use cache option to enable browser caching
                    cache: true,
                    success: function(resp) {
                        // Create a document fragment for better performance
                        data = resp
                            .filter(p => p != null) 
                            .map(function(p) {
                                // Pre-compute and store the words for faster searching
                                p.words = (p.title.toLowerCase() + ' ' + p.summary.toLowerCase()).match(/(\w+)/g) || [];
                                return p;
                            });
                        find(phrase);
                    }
                });
            }

            // Optimize filtering with early returns
            matches = data.filter(function(p) {
                // Skip processing if words array is empty
                if (!p.words || !p.words.length) return false;
                
                return phrase.filter(function(a) {
                    return p.words.some(function(b) {
                        return a === b || b.indexOf(a) === 0;
                    });
                }).length === phrase.length;
            });

            // Use document fragment for better DOM performance
            const fragment = document.createDocumentFragment();
            $(matches).each(function() {
                const li = document.createElement('li');
                li.innerHTML = '<h6>' + this.title + '</h6><p>' + this.title + '... <small><a href="' + this.url + '">Read more</a></small></p><hr>';
                fragment.appendChild(li);
            });
            
            $('#search-results', search).append(fragment);
            $('#search-results', search).show();
            $('#close', search).show();
        };

        function handleSearch() {
            $('#search-results', search).empty();
            $('#search-results', search).hide();
            $('#close', search).hide();

            var phrase = $('input', search).val();
            if (phrase.length >= 4) {
                const words = phrase.toLowerCase().match(/(\w+)/g);
                if (words && words.length) {
                    find(words);
                }
            }
            return false;
        }

        // Use passive event listeners where possible
        $('input', search).bind("focus", debounce(handleSearch, 100));

        $('#close', search).bind("click", function() {
            $('#search-results', search).hide();
            $('#close', search).hide();
            return false;
        });

        $('input', search).keyup(debounce(handleSearch, 100));
    };
    
    // Set the first character of string to uppercase
    function capitalize(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    
    // Surround data table rows generated in renderTable function with table head
    function tableHtml(content, domain = false, tableDomains) {
        return `<div class="p-1 bg-light"><strong>${domain ? capitalize(tableDomains) : ""}</strong></div>
                <table id="ont_table" class="table table-hover sortable">
                    <thead>
                        <tr>
                            <th scope="col" style="min-width: 4em;">
                                <span class="sort-button" title="Sort by ID" data-sort="id" >
                                    ID <i class="bi-chevron-up" aria-hidden="true"></i>
                                </span>
                            </th>
                            <th scope="col">
                                <span class="sort-button" title="Sort by name" data-sort="name" >
                                    Name <i class="bi-chevron-up" aria-hidden="true"></i>
                                </span>
                            </th>
                            <th scope="col">
                                <span>Description</span>
                            </th>
                            <th scope="col">
                                <span>Resource Type</span>
                            </th>
                            <th scope="col">
                                <span>Quick Access</span>
                            </th>
                            <th scope="col">
                                <span class="sort-button" title="Sort by status" data-sort="license" >
                                    License <i class="bi-chevron-up" aria-hidden="true"></i>
                                </span>
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
        const resourcetype = item.category ? 
                           item.category.replace(/([a-z])([A-Z])/g, '$1 $2') : 
                           '';
        const homepage = item.homepage_url || '#';
        const license_box = createLicenseBox(item);
        
        return `
            <tr class="${is_inactive}">
                <th scope="row">
                    <a href="resource/${id}/${id}.html">
                        ${id}
                    </a>
                </td>
                <td>
                    ${title}
                </td>
                <td>
                    <span style="background-color: #ff8d82">${is_obsolete}</span>
                    ${description}
                </td>
                <td>
                    ${resourcetype}
                </td>
                <td>
                    <div class="btn-group btn-group-sm" role="group">
                        <a class="btn btn-outline-primary" href="${homepage}" aria-label="Go to the homepage for ${title}" title="Go to the homepage for ${title}">
                            <i class="bi-house" aria-hidden="true"></i>
                        </a>
                        ${createPublicationButton(item, title)}
                    </div>
                </td>
                <td>
                    ${license_box}
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
    
    function createPublicationButton(item, title) {
        return (item.publications && item.publications.length > 0) ? 
            `<a role="button" class="btn btn-outline-primary" href="http://dx.doi.org/${item.publications[0].id}" aria-label="View the primary publication for ${title}" title="View the primary publication for ${title}">
                <i class="bi-book" aria-hidden="true"></i>
            </a>` : 
            `<a role="button" class="btn btn-outline-primary disabled">
                <i class="bi-book" aria-hidden="true"></i>
            </a>`;
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
    function renderTable(data, domain = false) {
        // Show loading indicator right away
        $tableDiv.html('<div class="loading-indicator">Loading resources...</div>');
        
        // Check if data is valid before processing
        if (!data || !Array.isArray(data) || data.length === 0) {
            $tableDiv.html('<div class="alert alert-info">No resources found - please try another search.</div>');
            $tableMain.css('display', 'block');
            return;
        }
        
        // Preprocess data before manipulation
        const processedData = data.map(item => {
            const id = item.id || '';
            const is_inactive = item.activity_status === "inactive" || item.activity_status === "orphaned" ? "inactive_row" : "";
            const is_obsolete = item.is_obsolete ? "(obsolete)" : 
                             (item.activity_status === "inactive" || item.activity_status === "orphaned") ? 
                             `(${item.activity_status})` : "";
            
            // Pre-compute domain for faster sorting
            const domainValue = item.domain ? item.domain.trim() : "Unknown";
            
            return {
                item,
                id,
                is_inactive,
                is_obsolete,
                domainValue
            };
        });
        
        // Separate dashboard data fetch from the rendering
        setTimeout(() => {
            renderBasicTable(processedData, domain);
        }, 0);
        
        // If dashboard data should be loaded, do it asynchronously
        if (typeof shouldFetchDashboardData !== 'undefined' && shouldFetchDashboardData) {
            setTimeout(() => {
                fetchAndProcessDashboardData(data);
            }, 50);
        }
    }
    
    // Render the basic table structure without waiting for dashboard data
    function renderBasicTable(processedData, domain) {
        // Check data again before processing
        if (!processedData || !Array.isArray(processedData) || processedData.length === 0) {
            $tableDiv.html('<div class="alert alert-info">No resources found matching your criteria.</div>');
            $tableMain.css('display', 'block');
            return;
        }
        
        let table = '';
        let domainTables = '';
        
        // Safely get unique domains
        let tableDomains = [];
        let tableDomainhtml = {};
        
        if (domain) {
            // Get unique domains safely
            const domainSet = new Set();
            processedData.forEach(item => {
                if (item && item.domainValue) {
                    domainSet.add(item.domainValue);
                }
            });
            tableDomains = Array.from(domainSet);
            
            // Prepare domain buckets
            tableDomains.forEach(domainName => {
                tableDomainhtml[domainName] = '';
            });
        }
        
        // Process in chunks for large datasets (improves responsiveness)
        const CHUNK_SIZE = 50;
        const processChunk = (startIndex) => {
            const endIndex = Math.min(startIndex + CHUNK_SIZE, processedData.length);
            
            for (let i = startIndex; i < endIndex; i++) {
                const item = processedData[i];
                // Skip undefined items
                if (!item) continue;
                
                const {item: originalItem, id, is_inactive, is_obsolete, domainValue} = item;
                const template = createTableRow(originalItem, id, is_inactive, is_obsolete);
                
                if (domain && domainValue) {
                    // Make sure the domain exists in our buckets
                    if (!tableDomainhtml[domainValue]) {
                        tableDomainhtml[domainValue] = '';
                    }
                    tableDomainhtml[domainValue] += template;
                } else {
                    table += template;
                }
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
            if (domain && tableDomains.length > 0) {
                // Sort domains
                tableDomains.sort();
                
                // Special case for "Upper" domain
                const upperIndex = tableDomains.findIndex(d => d && d.toLowerCase() === "upper");
                if (upperIndex > -1) {
                    const upperDomain = tableDomains.splice(upperIndex, 1)[0];
                    tableDomains.unshift(upperDomain);
                }
                
                // Build all tables at once
                tableDomains.forEach(domainName => {
                    if (domainName && tableDomainhtml[domainName]) {
                        domainTables += tableHtml(tableDomainhtml[domainName], true, domainName);
                    }
                });
                
                if (domainTables.length === 0) {
                    $tableDiv.html('<div class="alert alert-info">No resources found with the selected domain.</div>');
                } else {
                    $tableDiv.html(domainTables);
                }
            } else {
                if (table.length === 0) {
                    $tableDiv.html('<div class="alert alert-info">No resources found matching your criteria.</div>');
                } else {
                    $tableDiv.html(tableHtml(table, false, ""));
                }
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
            const domain = (row.domain || '').toLowerCase();
            const title = (row.title || '').toLowerCase();
            const description = (row.description || '').toLowerCase();
            
            // Check each field, return as soon as a match is found (faster)
            if (id.includes(term)) return true;
            if (domain.includes(term)) return true;
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
        
        // Check for empty data to avoid errors
        if (!data || !data.resources) return;
        
        // Filter in steps for better performance
        let filteredData = data.resources.filter(x => x.category !== undefined);
        
        // Only apply filters if values are selected
        if (selectedResourceType) {
            filteredData = filteredData.filter(x => x.category && x.category.includes(selectedResourceType));
        }
        
        if (selectedDomain) {
            filteredData = filteredData.filter(x => x.domain && x.domain.includes(selectedDomain));
        }
        
        // Apply search filter
        filteredData = Search($searchVal, filteredData);
        
        // Apply checkbox filters
        applyFilters(filteredData);
    }
    
    /**
     * Apply selected checkbox filter to data passed in
     * @param {object} data
     */
    function applyFilters(data) {
        const selector = $("[data-filter]");
        const domain = selector[0].checked;
        const hideactive = selector[1].checked;
        const hideObsolete = selector[2].checked;
        
        let filteredData = data;
        
        // Apply filters in a single pass
        if (hideactive || hideObsolete) {
            filteredData = data.filter(item => {
                // Skip items that should be hidden by activity status
                if (hideactive && item.activity_status !== "active") {
                    return false;
                }
                
                // Skip obsolete items if requested
                if (hideObsolete && item.is_obsolete === true) {
                    return false;
                }
                
                return true;
            });
        }
        
        // Sort if domain grouping is requested
        if (domain) {
            filteredData = sortByField(filteredData, "domain");
            renderTable(filteredData, true);
        } else {
            renderTable(filteredData);
        }
    }
    
    /**
     * Sort json ontology data by the given sort field
     * @param {Object} data
     * @param {string|number} sortField
     */
    function sortByField(data, sortField) {
        return data.sort(function(a, b) {
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
            
            // Extract domains (fix for duplication issue)
            const domains = [...new Set(
                data.resources
                    .filter(r => r.domain !== undefined)
                    .map(r => r.domain.trim())
            )];
            domains.sort();
            
            // Extract resource types (fix for duplication issue)
            const resourceTypes = [...new Set(
                data.resources
                    .filter(r => r.category !== undefined)
                    .map(r => r.category.trim())
            )];
            resourceTypes.sort();
            
            // Populate dropdowns (avoids duplication)
            populateDropdown("#dd-domains", domains);
            
            // Use the formatResourceType function for resource types dropdown
            populateDropdown("#dd-resourcetypes", resourceTypes, true, formatResourceType);
            
            // Render initial table
            renderTable(data.ontologies);
            
            // Set up event handlers with debounce
            const filterHandler = debounce(() => apply_all_filters(data), 100);
            
            $("[data-filter]").on("change", filterHandler);
            $ddDomains.on("change", filterHandler);
            $ddResourceTypes.on("change", filterHandler);
            $searchVal.on("keyup", filterHandler);
            
            // Create observer for table sorting
            const observer = new MutationObserver(function() {
                initSortableTables();
            });
            
            observer.observe($tableDiv[0], {
                childList: true,
                subtree: true
            });
            
            // Trigger initial filter
            $("[data-filter]").first().trigger('change');
        })
        .catch(error => {
            console.error('Error loading data:', error);
            $tableDiv.html('<div class="alert alert-danger">Failed to load data. Please try refreshing the page.</div>');
        });
});
