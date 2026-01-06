#!/usr/bin/env python3
"""
Generate automated evaluation pages from evals/evals_automated.tsv

This script reads evaluation data from evals_automated.tsv and generates
evaluation markdown pages with the 'made_by_ai: true' flag to indicate
they were generated automatically.

Usage:
    python util/generate_automated_evals.py
"""

import sys
import csv
import datetime
import re
import html
from pathlib import Path
from collections import OrderedDict
from urllib.parse import quote

import yaml

# Setup paths
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

def load_md(path):
    """Load a markdown file and return (front matter dict, content string)"""
    with open(path, 'r', encoding='utf-8') as f:
        contents = f.read()

    if not contents.startswith('---'):
        return {}, contents

    try:
        # Find the second --- separator
        end_idx = contents.find('---', 3)
        if end_idx == -1:
            return {}, contents

        fm_str = contents[3:end_idx].strip()
        md_str = contents[end_idx+3:].strip()

        fm = yaml.load(fm_str, Loader=yaml.SafeLoader) or {}
        return fm, md_str
    except Exception as e:
        print(f"WARN: could not parse frontmatter: {e}")
        return {}, contents


def create_automated_evaluation_pages():
    """
    Read evals/evals_automated.tsv and create automated evaluation pages
    with made_by_ai=true flag.
    """
    evals_path = ROOT / 'evals' / 'evals_automated.tsv'
    if not evals_path.exists():
        print(f"No {evals_path} found; skipping automated evaluation page generation")
        return

    print(f"Reading automated evaluations from {evals_path}")

    created = 0
    updated_links = 0

    with open(evals_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)

        if not rows or len(rows) < 3:
            print("evals_automated.tsv needs at least 3 rows (header categories, header questions, data)")
            return

        group_headers = rows[0]
        question_headers = rows[1]

        # Load human-readable question titles from eval_descriptions.tsv
        descriptions = {}
        desc_path = ROOT / 'evals' / 'eval_descriptions.tsv'
        if desc_path.exists():
            try:
                with open(desc_path, 'r', newline='', encoding='utf-8') as df:
                    d_reader = csv.reader(df, delimiter='\t')
                    for d_row in d_reader:
                        if not d_row or len(d_row) < 2:
                            continue
                        k = (d_row[0] or '').strip()
                        v = (d_row[1] or '').strip()
                        if not k or not v:
                            continue
                        descriptions[k] = v
            except Exception as e:
                print(f"WARN: could not read eval_descriptions.tsv: {e}")

        def humanize_identifier(s: str) -> str:
            t = (s or '').strip()
            if not t:
                return ''
            t = t.replace('_', ' ')
            t = t.title()
            t = t.replace('Kg', 'KG').replace('Api', 'API').replace('Id', 'ID').replace('Ids', 'IDs')
            return t

        def display_title(key: str) -> str:
            return descriptions.get(key, humanize_identifier(key))

        def style_for_value(val: str) -> str:
            v = (val or '').strip().lower()
            if v.startswith('y') or v.startswith('yes'):
                return 'background-color:#d4edda;'
            if v.startswith('n') or v.startswith('no'):
                return 'background-color:#f8d7da;'
            return ''

        def linkify_and_escape(s: str) -> str:
            if not s:
                return ''
            pattern = re.compile(r'(https?://[^\s<>\"]+)')
            parts = []
            last = 0
            for m in pattern.finditer(s):
                parts.append(html.escape(s[last:m.start()]))
                url = m.group(1)
                url_esc = html.escape(url)
                parts.append(f'<a href="{url_esc}">{url_esc}</a>')
                last = m.end()
            parts.append(html.escape(s[last:]))
            return ''.join(parts)

        def clean_comment(c: str) -> str:
            if not c:
                return ''
            txt = c.strip()
            txt = re.sub(r'^\s*(yes|y|no|n)\b[\s:;\-–—]*', '', txt, flags=re.IGNORECASE)
            txt = re.sub(r'^[YyNn],\s+', '', txt)
            txt = re.sub(r'^[,\s]+', '', txt)
            txt = txt.strip()
            if len(txt) >= 2 and txt[0] == '(' and txt[-1] == ')':
                txt = txt[1:-1].strip()
            if txt:
                txt = txt[0].upper() + txt[1:]
            return txt

        # Forward-fill empty group headers
        filled_group_headers = list(group_headers)
        last = ''
        for i in range(len(filled_group_headers)):
            current = (filled_group_headers[i] or '').strip()
            if current:
                last = current
            else:
                filled_group_headers[i] = last

        # Process data rows
        for row in rows[2:]:
            if not row or len(row) == 0:
                continue

            rid = (row[0] or '').strip()
            if not rid:
                continue

            res_dir = ROOT / 'resource' / rid
            res_file = res_dir / f"{rid}.md"

            if not res_file.exists():
                print(f"WARN: evaluation provided for '{rid}' but no resource page found; skipping")
                continue

            # Group questions by category
            grouped = OrderedDict()
            col_limit = min(len(filled_group_headers), len(question_headers), len(row))
            evaluator_val = ''
            evaluation_date_val = ''

            for i in range(1, col_limit):
                cat = (filled_group_headers[i] or '').strip()
                q = (question_headers[i] or '').strip()
                v = (row[i] or '').strip()

                if not q and not v:
                    continue

                q_norm = (q or '').strip().lower()
                if q_norm == 'evaluator':
                    evaluator_val = v
                    continue
                if q_norm in ('evaluation_date', 'evaluation date', 'date'):
                    evaluation_date_val = v
                    continue

                is_comment = False
                base_q = q
                if q.endswith('_text'):
                    is_comment = True
                    base_q = q[:-5]

                if cat not in grouped:
                    grouped[cat] = OrderedDict()
                if base_q not in grouped[cat]:
                    grouped[cat][base_q] = {
                        'question': base_q,
                        'answer': '',
                        'comment': ''
                    }

                if is_comment:
                    grouped[cat][base_q]['comment'] = v
                else:
                    grouped[cat][base_q]['answer'] = v

            # Set defaults
            if not evaluation_date_val:
                evaluation_date_val = datetime.date.today().isoformat()
            if not evaluator_val:
                evaluator_val = 'Automated Evaluation'

            # Build HTML content
            html_lines = []
            for cat, qmap in grouped.items():
                if cat:
                    html_lines.append(f"## {cat}")
                html_lines.append("<div class=\"table-responsive\">")
                html_lines.append("<table class=\"table table-striped\">")
                html_lines.append("<thead><tr><th>Question</th><th>Answer</th><th>Comment</th></tr></thead><tbody>")
                yes_count = 0
                answered_count = 0

                for base_q, entry in qmap.items():
                    q_val = display_title(entry.get('question', ''))
                    a_val = entry.get('answer', '')
                    c_val = clean_comment(entry.get('comment', ''))
                    q_esc = linkify_and_escape(q_val or '')
                    a_esc = linkify_and_escape(a_val or '')
                    c_esc = linkify_and_escape(c_val or '')
                    style = style_for_value(a_val)
                    style_attr = f" style=\"{style}\"" if style else ""
                    v_norm = (a_val or '').strip().lower()

                    if v_norm:
                        answered_count += 1
                        if v_norm.startswith('y') or v_norm.startswith('yes'):
                            yes_count += 1

                    html_lines.append(
                        f"<tr><td>{q_esc}</td><td{style_attr}>{a_esc}</td><td>{c_esc}</td></tr>")

                html_lines.append("</tbody></table></div>")

                if (cat or '').strip().lower() != 'license information':
                    html_lines.append(
                        f"<p><strong>Section Score:</strong> {yes_count}/{answered_count}</p>")
                html_lines.append("")

            content = "\n".join(html_lines) + "\n"

            # Write the evaluation page with made_by_ai flag
            eval_md_path = res_dir / f"{rid}_eval_automated.md"

            with open(eval_md_path, 'w', encoding='utf-8') as ef:
                fm = {
                    'layout': 'eval_detail',
                    'evaluator': evaluator_val or None,
                    'evaluation_date': evaluation_date_val,
                    'made_by_ai': True,
                }
                fm = {k: v for k, v in fm.items() if v is not None}
                ef.write("---\n")
                yaml.dump(fm, ef)
                ef.write("---\n\n")
                ef.write(content)

            print(f"✅ Created automated evaluation page for {rid} at {eval_md_path}")
            created += 1

            # Add link to resource page if missing
            try:
                (metadata, md) = load_md(res_file)
                link_snippet = f"[{rid} automated evaluation]({rid}_eval_automated.html)"
                if link_snippet not in md:
                    md_update = md.rstrip() + "\n\n## Automated Evaluation\n\n- View the automated evaluation: " + link_snippet + "\n"
                    with open(res_file, 'w', encoding='utf-8') as rf:
                        rf.write("---\n")
                        yaml.dump(metadata, rf)
                        rf.write("---\n")
                        rf.write(md_update)
                    updated_links += 1
                    print(f"   Updated resource page with automated evaluation link")
            except Exception as e:
                print(f"   WARN: could not update resource page for {rid}: {e}")

    print(f"\n✅ Created {created} automated evaluation page(s); updated {updated_links} resource page link(s)")


if __name__ == '__main__':
    create_automated_evaluation_pages()
