# Site Development

This documentation is for developers of the KG-Registry site.

This version of the site is based on the OBO Foundry site (<https://obofoundry.org/>).

## Getting Started

Because Jekyll can be difficult to install, Docker provides an
alternative for running the `serve` command, then open http://localhost:4000:

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve
```

For features that use WebAssembly and Web Workers (like the Advanced Search), use the `--host` parameter to avoid CORS issues:

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve --host=0.0.0.0
```

Then access the site using your machine's IP address instead of localhost.

### Troubleshooting Module Resolution Issues

If you encounter module resolution errors like:

```
Failed to resolve module specifier "apache-arrow". Relative references must start with either "/", "./", or "../".
```

Or errors like:

```
Uncaught ReferenceError: exports is not defined
```

The advanced-search.html file is now configured to load Apache Arrow as a global UMD module and DuckDB from a CDN with fallback mechanisms. This approach avoids module resolution issues and compatibility problems with Node.js specific code in browser environments.

The site is configured to load these dependencies from CDNs:
- Apache Arrow is loaded from: `https://cdn.jsdelivr.net/npm/apache-arrow@17.0.0/Arrow.js`
- DuckDB modules are loaded from: `https://cdn.jsdelivr.net/npm/@duckdb/duckdb-wasm@1.29.0/dist/`

Local copies of DuckDB worker scripts and WASM files are still important to avoid CORS issues:

```shell
# Create directories
mkdir -p assets/js/duckdb

# Download DuckDB files
curl -s https://cdn.jsdelivr.net/npm/@duckdb/duckdb-wasm@1.29.0/dist/duckdb-browser-mvp.worker.js -o assets/js/duckdb/duckdb-browser-mvp.worker.js
curl -s https://cdn.jsdelivr.net/npm/@duckdb/duckdb-wasm@1.29.0/dist/duckdb-mvp.wasm -o assets/js/duckdb/duckdb-mvp.wasm
```f the site is based on the OBO Foundry site (<https://obofoundry.org/>).

## Getting Started

Because Jekyll can be difficult to install, Docker provides an
alternative for running the `serve` command, then open http://localhost:4000:

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve
```

For features that use WebAssembly and Web Workers (like the Advanced Search), use the `--host` parameter to avoid CORS issues:

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve --host 0.0.0.0
```

Then access the site using your machine's IP address instead of localhost.

You can make changes locally and the Docker image will automatically update.
When you're ready, you can commit to a new branch and send a pull request.
After it's accepted, it will be automatically built and deployed to
https://kghub.org/kg-registry/ in a few minutes.

## Details

The setup is fairly standard for Jekyll. We use Jekyll bootstrap
(bootstrap 3). We try and keep things minimal so that the site will
work on github. Even if you have no knowledge of Jekyll, it is fairly
easy to introspect what is going on if you have done much CMS work or
web development.

Basically, every `.md` or `.html` file in the directory is visible on
the site, the same path. `.md` files are automatically translated to
`.html`.

Jekyll uses a templating system called liquid. The basic idea is
simple, templating commands are contained within braces '{ }'.

Pages can have different layouts - see the [_layouts/](_layouts/)
directory. They can also include templates from the
[_includes/](_includes/) directory.

See [assets/themes](assets/themes) for bootstrap styling - don't touch this unless
you know what you're doing.

## Advanced Search Feature

The site includes an advanced search feature that allows users to run SQL queries directly against the KG Registry data using DuckDB-WASM (WebAssembly version of DuckDB that runs in the browser). This feature is available at `/kg-registry/advanced-search.html`.

### Parquet Files (Recommended)

The KG Registry data is now compiled into Parquet files located in the `/registry/parquet/` directory. These files are generated from the registry data and contain tables for resources, products, domains, and other metadata. Parquet is a columnar storage format that provides better compression and query performance than a full database file, while being more Git-friendly.

### Updating the Parquet Files

If you make changes to the registry data and need to regenerate the Parquet files, use the following command:

```shell
# Export registry data to Parquet files
python -m kg_registry.cli parquet sync --yaml-file registry/kgs.yml --output-dir registry/parquet
```

### Legacy DuckDB Database (Deprecated)

The previous approach used a full DuckDB database file located at `/registry/kg_registry.duckdb`. This approach is being phased out in favor of Parquet files, but is still supported for backward compatibility.

To update the legacy DuckDB database:

```shell
# Export registry data to DuckDB
python -m kg_registry.cli duckdb sync --yaml-file registry/kgs.yml --db-path registry/kg_registry.duckdb
```

### Advanced Search Page

The advanced search page (`advanced-search.html`) uses DuckDB-WASM to load and query the database file directly in the browser. This allows users to run complex SQL queries without any server-side processing.

The page includes:
- A SQL query editor
- Example queries to help users get started
- Results display in a table format
- CSV export functionality for query results
- Database schema information

#### Dependencies

The Advanced Search feature depends on:
- DuckDB-WASM v1.29.0
- Apache Arrow v17.0.0

These dependencies are loaded from local files in the `assets/js/duckdb/` and `assets/js/apache-arrow/` directories with fallback to CDN versions if local files are not available.

### Running with Docker to Avoid CORS Issues

The Advanced Search feature uses WebAssembly and Web Workers, which may encounter CORS (Cross-Origin Resource Sharing) issues when running locally. To avoid these issues, use the Docker command with the host parameter:

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve --host 0.0.0.0
```

Then access the site using the Docker host's IP address rather than localhost, e.g., http://192.168.1.100:4000/kg-registry/

## Code quality

1. Install the Node Package Manager (NPM) following [these instructions](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
2. Install the [node package exector (`npx`)](https://www.npmjs.com/package/npx) with NPM using `npm install npx`
3. Install [`prettier`](https://prettier.io) with NPM using `npm install prettier`
4. Run `prettier` from the root of the repository with `npx prettier --write .`
