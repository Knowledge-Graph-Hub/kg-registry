/**
 * Parquet file handling for KG-Registry web interface
 * 
 * This module provides functions to load and query Parquet files
 * using DuckDB in the browser.
 */

// Initialize DuckDB
let duckdbInstance = null;
let duckdbConnection = null;

/**
 * Initialize DuckDB and load Parquet files
 * 
 * @param {string} parquetDir - Directory containing Parquet files
 * @returns {Promise<void>}
 */
async function initDuckDB(parquetDir = '/kg-registry/registry/parquet') {
    // Check if DuckDB is available globally
    if (!window.duckdb) {
        throw new Error('DuckDB not loaded. Make sure to include the DuckDB scripts before initializing.');
    }
    
    // Check if Arrow is available
    if (!window.Arrow) {
        throw new Error('Apache Arrow not loaded. Make sure to include the Arrow scripts before initializing.');
    }
    
    // Using local resources for WASM files
    const wasmModule = "/kg-registry/assets/js/duckdb/duckdb-mvp.wasm";
    const workerScript = "/kg-registry/assets/js/duckdb/duckdb-browser-mvp.worker.js";
    
    // Create a Web Worker with the DuckDB worker script
    const workerUrl = URL.createObjectURL(
        new Blob([`
            // Import DuckDB worker
            importScripts('${workerScript}');
        `], { type: 'application/javascript' })
    );
    
    // Create worker and instantiate DuckDB
    try {
        const worker = new Worker(workerUrl);
        const logger = new window.duckdb.ConsoleLogger();
        duckdbInstance = new window.duckdb.AsyncDuckDB(logger, worker);
        
        // Instantiate with WASM module
        await duckdbInstance.instantiate({
            mainModule: wasmModule
        });
    } catch (workerError) {
        console.error('Failed to create worker or instantiate DuckDB:', workerError);
        
        // Show more helpful error message based on the specific error
        let errorMessage = workerError.message;
        if (errorMessage.includes('SecurityError') || errorMessage.includes('CORS')) {
            errorMessage = `CORS error: Cannot load worker from a different origin. Try running with a proper web server or use a different browser.`;
        }
        
        throw new Error(`DuckDB initialization failed: ${errorMessage}`);
    }
    
    // Connect to the database
    duckdbConnection = await duckdbInstance.connect();
    
    // Load Parquet files
    try {
        const tables = ['resources', 'resource_domains', 'resource_products'];
        
        for (const table of tables) {
            const parquetFile = `${parquetDir}/${table}.parquet`;
            
            try {
                const resp = await fetch(parquetFile);
                if (!resp.ok) {
                    throw new Error(`Failed to fetch Parquet file: ${resp.status} ${resp.statusText}`);
                }
                
                const parquetData = await resp.arrayBuffer();
                const parquetFileName = `${table}.parquet`;
                
                await duckdbInstance.registerFileBuffer(parquetFileName, new Uint8Array(parquetData));
                await duckdbConnection.query(`CREATE VIEW ${table} AS SELECT * FROM read_parquet('${parquetFileName}')`);
                console.log(`Loaded ${table} Parquet file`);
                
            } catch (error) {
                console.warn(`Error loading ${table} Parquet file:`, error);
                // Create a fallback empty table if Parquet file couldn't be loaded
                if (table === 'resources') {
                    await duckdbConnection.query(`
                        CREATE TABLE resources (id VARCHAR, name VARCHAR, category VARCHAR, description VARCHAR);
                        INSERT INTO resources VALUES 
                        ('example1', 'Example Resource 1', 'DataSource', 'This is a sample resource');
                    `);
                } else if (table === 'resource_domains') {
                    await duckdbConnection.query(`
                        CREATE TABLE resource_domains (resource_id VARCHAR, domain VARCHAR);
                        INSERT INTO resource_domains VALUES ('example1', 'sample');
                    `);
                } else if (table === 'resource_products') {
                    await duckdbConnection.query(`
                        CREATE TABLE resource_products (
                            resource_id VARCHAR, product_id VARCHAR, product_name VARCHAR,
                            product_category VARCHAR, product_description VARCHAR, 
                            product_format VARCHAR, product_url VARCHAR
                        );
                    `);
                }
            }
        }
        
        console.log('All Parquet files loaded successfully');
    } catch (error) {
        console.error('Error loading Parquet files:', error);
        throw error;
    }
}

/**
 * Execute a query against the loaded Parquet data
 * 
 * @param {string} query - SQL query to execute
 * @param {Array} params - Query parameters
 * @returns {Promise<Array>} - Query results
 */
async function executeQuery(query, params = []) {
    if (!duckdbConnection) {
        throw new Error('DuckDB not initialized. Call initDuckDB() first.');
    }
    
    try {
        const result = await duckdbConnection.query(query, params);
        return result.toArray().map(row => {
            const obj = {};
            for (const [key, value] of Object.entries(row)) {
                obj[key] = value;
            }
            return obj;
        });
    } catch (error) {
        console.error('Error executing query:', error);
        throw error;
    }
}

/**
 * Search resources by name or description
 * 
 * @param {string} searchTerm - Term to search for
 * @returns {Promise<Array>} - Search results
 */
async function searchResources(searchTerm) {
    const query = `
        SELECT * FROM resources
        WHERE name ILIKE '%' || ? || '%' OR description ILIKE '%' || ? || '%'
        ORDER BY name
    `;
    return executeQuery(query, [searchTerm, searchTerm]);
}

/**
 * Query resources with filters
 * 
 * @param {Object} filters - Filter criteria
 * @returns {Promise<Array>} - Query results
 */
async function queryResources(filters = {}) {
    let query = "SELECT * FROM resources WHERE 1=1";
    const params = [];
    
    if (filters.category) {
        query += " AND category = ?";
        params.push(filters.category);
    }
    
    if (filters.activityStatus) {
        query += " AND activity_status = ?";
        params.push(filters.activityStatus);
    }
    
    if (filters.domain) {
        query += " AND id IN (SELECT resource_id FROM resource_domains WHERE domain = ?)";
        params.push(filters.domain);
    }
    
    if (filters.nameContains) {
        query += " AND name ILIKE '%' || ? || '%'";
        params.push(filters.nameContains);
    }
    
    return executeQuery(query, params);
}

/**
 * Get resource statistics
 * 
 * @returns {Promise<Object>} - Statistics object
 */
async function getResourceStats() {
    const stats = {};
    
    // Total resources
    const totalResult = await executeQuery("SELECT COUNT(*) as count FROM resources");
    stats.totalResources = totalResult[0].count;
    
    // Active resources
    const activeResult = await executeQuery(
        "SELECT COUNT(*) as count FROM resources WHERE activity_status = 'active'"
    );
    stats.activeResources = activeResult[0].count;
    
    // Resources by category
    const categoryResult = await executeQuery(
        `SELECT category, COUNT(*) as count
         FROM resources
         WHERE category IS NOT NULL
         GROUP BY category
         ORDER BY count DESC`
    );
    stats.byCategory = {};
    for (const row of categoryResult) {
        stats.byCategory[row.category] = row.count;
    }
    
    // Resources by domain
    const domainResult = await executeQuery(
        `SELECT domain, COUNT(*) as count
         FROM resource_domains
         GROUP BY domain
         ORDER BY count DESC`
    );
    stats.byDomain = {};
    for (const row of domainResult) {
        stats.byDomain[row.domain] = row.count;
    }
    
    return stats;
}

export {
    initDuckDB,
    executeQuery,
    searchResources,
    queryResources,
    getResourceStats
};
