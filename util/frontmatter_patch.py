#!/usr/bin/env python3
"""
Minimal-diff writes of YAML frontmatter back to resource pages.

The concat step updates resource pages (propagated products, normalized
sources, deduplicated warnings, ...). Re-dumping the whole frontmatter with
``yaml.dump`` re-wraps every description, re-indents lists and drops the
trailing newline, so pages that changed in one product block show a diff
on every line (issue #934).

``write_frontmatter_minimal`` instead splices only what changed into the
page's existing text:

* a page whose metadata and body are unchanged is not written at all;
* unchanged top-level keys, product list items and item keys keep their
  original text byte-for-byte;
* a changed key, or a new product, is emitted with ``yaml.dump`` and indented
  to match the page's own list style;
* the markdown body is kept verbatim unless its content changed.

The patched text is parsed back and compared with the intended metadata. If
that ever fails to match (unusual YAML such as anchors, flow collections, or
comments in the way), the page is written with the old full dump instead.
"""

import pathlib
import re
from typing import Any, List, Optional, Tuple

import yaml

__all__ = ["write_frontmatter_minimal", "patch_frontmatter_text"]

_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---[ \t]*(?:\n|\Z)(.*)\Z", re.DOTALL)
_KEY_RE = re.compile(r"([A-Za-z_][\w\-]*):(?:[ \t]|$)")


class _NoAliasDumper(yaml.Dumper):
    """yaml.Dumper that never emits &anchors/*aliases for shared objects."""

    def ignore_aliases(self, data):
        return True


def _dump(value: Any) -> List[str]:
    text = yaml.dump(value, Dumper=_NoAliasDumper, allow_unicode=True, default_flow_style=False)
    return text.rstrip("\n").split("\n")


def _full_dump(metadata: dict) -> str:
    return yaml.dump(metadata, allow_unicode=True)


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _split_keys(lines: List[str], indent: int) -> Optional[Tuple[List[str], List[Tuple[str, int, int]]]]:
    """Split mapping lines at ``indent`` into (prefix, [(key, start, end), ...]).

    Returns None if the lines don't look like a plain block mapping.
    """
    pad = " " * indent
    segments: List[Tuple[str, int, int]] = []
    prefix_end = 0
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith(pad) and not line.startswith(pad + " "):
            rest = line[indent:]
            m = _KEY_RE.match(rest)
            if m:
                if segments:
                    key, start, _ = segments[-1]
                    segments[-1] = (key, start, i)
                else:
                    prefix_end = i
                segments.append((m.group(1), i, len(lines)))
                continue
            if rest.startswith("- ") or rest == "-" or rest.startswith("#"):
                if not segments:
                    return None
                continue
            return None
        if _indent_of(line) < indent:
            return None
        if not segments:
            return None
    if not segments:
        return None
    # trailing blank lines stay with the last key
    return lines[:prefix_end], segments


def _dict_items(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(v, dict) and isinstance(v.get("id"), str) for v in value)
        and len({v["id"] for v in value}) == len(value)
    )


def _emit_key(key: str, value: Any, indent: int) -> List[str]:
    pad = " " * indent
    return [pad + line if line else line for line in _dump({key: value})]


def _patch_mapping(lines: List[str], indent: int, old: dict, new: dict) -> Optional[List[str]]:
    split = _split_keys(lines, indent)
    if split is None:
        return None
    prefix, segments = split
    seen = [k for k, _, _ in segments]
    if len(set(seen)) != len(seen) or set(seen) != set(old):
        return None

    blocks = {}
    for key, start, end in segments:
        block = lines[start:end]
        if key not in new:
            continue
        if old[key] == new[key]:
            blocks[key] = block
            continue
        patched = None
        if isinstance(old[key], dict) and isinstance(new[key], dict):
            patched = _patch_nested_mapping(key, block, indent, old[key], new[key])
        elif _dict_items(old[key]) and _dict_items(new[key]):
            patched = _patch_item_list(block, indent, old[key], new[key])
        if patched is None and _is_extension(old[key], new[key]):
            patched = _append_list_items(block, indent, new[key][len(old[key]):])
        blocks[key] = patched if patched is not None else _emit_key(key, new[key], indent)

    order = [k for k in seen if k in new]
    for key in sorted(k for k in new if k not in old):
        blocks[key] = _emit_key(key, new[key], indent)
        pos = next((i for i, k in enumerate(order) if k > key), len(order))
        order.insert(pos, key)

    out = list(prefix)
    for key in order:
        out.extend(blocks[key])
    return out


def _patch_nested_mapping(key: str, block: List[str], indent: int, old: dict, new: dict) -> Optional[List[str]]:
    head = block[0][indent:]
    if head.rstrip() != f"{key}:":
        return None
    body = block[1:]
    first = next((l for l in body if l.strip()), None)
    if first is None or _indent_of(first) <= indent:
        return None
    patched = _patch_mapping(body, _indent_of(first), old, new)
    return None if patched is None else [block[0]] + patched


def _is_extension(old: Any, new: Any) -> bool:
    return isinstance(old, list) and isinstance(new, list) and len(new) > len(old) > 0 and new[: len(old)] == old


def _append_list_items(block: List[str], indent: int, extra: list) -> Optional[List[str]]:
    """Keep a block list's existing text and append ``extra`` items after it."""
    first = next((l for l in block[1:] if l.strip()), None)
    if first is None or block[0][indent:].rstrip().endswith(":") is False:
        return None
    item_indent = _indent_of(first)
    if item_indent < indent or not first[item_indent:].startswith("- "):
        return None
    end = len(block)
    while end > 1 and not block[end - 1].strip():
        end -= 1
    pad = " " * item_indent
    return block[:end] + [pad + l if l else l for l in _dump(extra)] + block[end:]


def _patch_item_list(block: List[str], indent: int, old: list, new: list) -> Optional[List[str]]:
    """Patch a list of {id: ...} mappings item by item."""
    body = block[1:]
    first = next((l for l in body if l.strip()), None)
    if first is None or block[0][indent:].rstrip().endswith(":") is False:
        return None
    item_indent = _indent_of(first)
    if item_indent < indent or not first[item_indent:].startswith("- "):
        return None
    dash = " " * item_indent + "- "

    starts = [i for i, l in enumerate(body) if l.startswith(dash)]
    if len(starts) != len(old) or starts[0] != body.index(first):
        return None
    items = {}
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(body)
        items[old[n]["id"]] = (old[n], body[start:end])

    key_indent = item_indent + 2
    out = [block[0]] + body[: starts[0]]
    for item in new:
        if item["id"] in items:
            old_item, lines = items[item["id"]]
            if old_item == item:
                out.extend(lines)
                continue
            as_mapping = [" " * key_indent + lines[0][key_indent:]] + lines[1:]
            patched = _patch_mapping(as_mapping, key_indent, old_item, item)
            if patched is not None:
                lead = next(i for i, l in enumerate(patched) if l.strip())
                patched[lead] = dash + patched[lead][key_indent:]
                out.extend(patched)
                continue
        pad = " " * item_indent
        out.extend(pad + l if l else l for l in _dump([item]))
    return out


def patch_frontmatter_text(text: str, metadata: dict, md: str) -> Optional[str]:
    """Return ``text`` with its frontmatter/body updated minimally, or None to fall back.

    Returns ``text`` itself when nothing changed.
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm, body = m.group(1), m.group(2)
    try:
        old = yaml.safe_load(fm)
    except yaml.YAMLError:
        return None
    if not isinstance(old, dict):
        return None

    new_body = body if body.strip() == (md or "").strip() else md
    if old == metadata:
        new_fm = fm
    else:
        patched = _patch_mapping(fm.rstrip("\n").split("\n"), 0, old, metadata)
        if patched is None:
            return None
        new_fm = "\n".join(patched) + "\n"
        try:
            if yaml.safe_load(new_fm) != metadata:
                return None
        except yaml.YAMLError:
            return None
    return "---\n" + new_fm + "---\n" + new_body


def write_frontmatter_minimal(path, metadata: dict, md: str) -> bool:
    """Write ``metadata`` and ``md`` to ``path`` with the smallest diff possible.

    Returns True if the file was written, False if it was already up to date.
    """
    path = pathlib.Path(path)
    text = path.read_text(encoding="utf-8") if path.exists() else None
    new_text = patch_frontmatter_text(text, metadata, md) if text is not None else None
    if new_text is None:
        new_text = "---\n" + _full_dump(metadata) + "---\n" + (md or "")
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True
