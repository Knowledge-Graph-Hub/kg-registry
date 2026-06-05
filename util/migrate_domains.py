#!/usr/bin/env python3
"""One-off migration for issue #601: remap resource `domains` to the
restructured DomainEnum.

Rewrites only the `domains:` list inside each main resource page's YAML
frontmatter, preserving indentation style and all other content so diffs
stay minimal. Applies the old->new mapping, drops values no longer in the
enum, de-duplicates while preserving order, and reports anything unmapped.
"""
import glob
import re
import sys

# old domain value -> new domain value (None means drop entirely)
MAPPING = {
    "health": "biomedical",
    "translational": "biomedical",
    "digital health": "information technology",
    "microbiome": "microbiology",
    "social determinants": "public health",
    "food science": "agriculture",
    "plant science": "agriculture",
    "upper": "general",
    "investigations": "general",
    "simulation": "information technology",
    "synthetic biology": "biological systems",
}

# Final permissible DomainEnum values (kept as-is when encountered)
ALLOWED = {
    "agriculture", "anatomy and development", "biological systems", "biomedical",
    "chemistry and biochemistry", "clinical", "drug discovery", "environment",
    "general", "genomics", "immunology", "information technology", "literature",
    "medical imaging", "microbiology", "neuroscience", "nutrition", "organisms",
    "other", "pathways", "pharmacology", "phenotype", "precision medicine",
    "proteomics", "public health", "systems biology", "toxicology", "stub",
}

ITEM_RE = re.compile(r"^(?P<indent>\s*)-\s+(?P<val>.+?)\s*$")


def remap(values):
    out = []
    for v in values:
        key = v.strip().strip("'\"").lower()
        new = MAPPING.get(key, key)
        if new is None:
            continue
        if new not in ALLOWED:
            # leave genuinely-unknown values untouched so they surface in validation
            new = key
        if new not in out:
            out.append(new)
    return out


def process(path):
    text = open(path).read()
    lines = text.split("\n")
    # locate frontmatter bounds
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None

    # find `domains:` within frontmatter
    dom_idx = None
    for i in range(1, end):
        if re.match(r"^domains:\s*$", lines[i]):
            dom_idx = i
            break
    if dom_idx is None:
        return None

    # collect contiguous list items
    j = dom_idx + 1
    items = []
    item_indent = None
    while j < end:
        m = ITEM_RE.match(lines[j])
        if not m:
            break
        if item_indent is None:
            item_indent = m.group("indent")
        items.append(m.group("val"))
        j += 1
    if not items:
        return None

    new_vals = remap(items)
    new_block = [f"{item_indent}- {v}" for v in new_vals]
    old_block = lines[dom_idx + 1:j]
    if old_block == new_block:
        return None  # no change

    new_lines = lines[:dom_idx + 1] + new_block + lines[j:]
    open(path, "w").write("\n".join(new_lines))
    return (items, new_vals)


def main():
    changed = 0
    for path in sorted(glob.glob("resource/*/*.md")):
        base = path.rsplit("/", 1)[1][:-3]
        folder = path.split("/")[1]
        if base != folder:
            continue  # only main resource pages carry domains
        res = process(path)
        if res:
            changed += 1
            old, new = res
            print(f"{folder}: {old} -> {new}")
    print(f"\nChanged {changed} resource pages.")


if __name__ == "__main__":
    sys.exit(main())
