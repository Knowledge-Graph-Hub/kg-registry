---
name: kg-registry-product-url-update
description: Use when updating the URL for a specific KG-Registry product, especially when the original URL is dead, redirected, versioned, or replaced by a newer canonical landing or download page.
---

# kg-registry-product-url-update

Update a stale or incorrect `product_url` for a specific KG-Registry product while preserving the intended identity of the product.

## When to use

- The user asks to fix or update the URL for a named product.
- A product URL is dead, redirects somewhere unexpected, or no longer matches the intended product.
- The old URL pointed to a version-specific artifact, but only a newer or more general live URL is now available.
- A validation or review pass finds an outdated product link that needs curation judgment rather than a mechanical replacement.

Skip when:

- The whole resource page needs broad curation rather than a focused product URL repair.
- The product itself is mis-modeled and needs to be split, renamed, or re-categorized first.
- The task is about generated files under `registry/` rather than source files under `resource/`.

## Inputs

- Required: a specific product identifier, or a resource file plus enough detail to identify the target product.
- Preferred: the owning resource file under `resource/<id>/<id>.md`.

If multiple products in the same file could match, resolve the exact target before editing.

## Workflow

1. Resolve the owning resource file and target product.
   - Find the resource page under `resource/<id>/<id>.md`.
   - Identify the exact product entry by `id`, `name`, `description`, or current `product_url`.
   - Read the surrounding product metadata before changing the URL.

2. Determine what the product is supposed to represent.
   - Use the product `id`, `name`, `description`, `format`, provenance, and any version fields to infer the intended artifact.
   - Distinguish between these common cases:
     - a stable landing page or portal
     - a versioned downloadable file
     - an API endpoint
     - a release directory or canonical "latest" location
   - Do not replace a URL blindly just because it is live. The replacement must still correspond to the same product concept.

3. Search for the best current live URL.
   - Expect web search to be necessary in many cases.
   - Start with authoritative sources: the resource homepage, official documentation, release notes, repository releases, download pages, API docs, and the hosting organization's site.
   - Use lightweight URL checks for candidate links when helpful, but prefer human-readable confirmation from official pages over status-code checking alone.
   - Treat redirects carefully. A redirect to a generic homepage may be less accurate than a stable download or release page.

4. Choose the replacement URL based on product identity, not only string similarity.
   - Prefer the closest live URL that still represents the same product.
   - If the old URL pointed to a specific version and that exact version is gone, a URL for the current version or canonical latest-download page can be acceptable.
   - If only a broader landing page remains, use it only when it is the best stable path to the same product and the file-specific URL no longer exists.
   - If the replacement materially changes what the product represents, stop and reconsider whether the product metadata itself also needs updating.

5. Update nearby metadata when the URL change implies it.
   - If the new URL clearly points to a newer version, update `latest_version` or version-related description text when supported by evidence.
   - If the product is now accessed through a landing page rather than a direct file, make sure the `description` still accurately explains what the user reaches there.
   - Update the parent resource's `last_modified_date` to today, since a product URL change is still a curation edit to the resource page.
   - Preserve existing provenance unless the source relationship itself has changed.
   - Do not rewrite unrelated parts of the resource page.

6. Validate the result.
   - After editing, consult the `kg-registry-validation` skill.
   - Run:
     ```bash
     uv run make validate-file FILE=resource/<id>/<id>.md
     ```
   - If formatting drifted, run prettify first and validate again.

## Heuristics

- Prefer official current URLs over mirrors unless the mirror is already the established product host.
- Prefer durable landing pages over brittle deep links when the deep link no longer exists.
- Prefer DOI or stable release URLs when they truly identify the same product release.
- Prefer canonical `latest/` endpoints only when the product is conceptually "current release" rather than a frozen historical version.
- If the old product was explicitly version-specific and only a new-version URL exists, keep the product only if the product description already tolerates that semantic shift or can be updated narrowly and truthfully.

## Common mistakes

- Replacing a dead URL with the resource homepage even though a more specific product page still exists.
- Updating the URL to a different product just because its filename looks similar.
- Treating any HTTP 200 response as sufficient evidence that the link is correct.
- Keeping stale version-specific description text after changing the URL to a newer release.
- Changing provenance fields when only the access URL changed.

## Relationship to other skills

- `kg-registry-curation` covers broader resource-page editing.
- `kg-registry-validation` should be used after the URL update to validate the edited file.