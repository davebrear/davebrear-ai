#!/usr/bin/env python3
"""Generate graph.json from the vault's wiki-links.

Usage:
    python tools/generate-graph.py

Outputs graph.json in the repo root. This file is used by the
interactive graph viewer (see tools/graph.html).
"""

import os
import re
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

nodes = []
edges = []
file_map = {}

for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'tools']
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.relpath(os.path.join(root, f), BASE)
        name = f.replace('.md', '')
        folder = path.split(os.sep)[0]
        file_map[name.lower()] = {'path': path, 'name': name, 'folder': folder}

for key, info in file_map.items():
    filepath = os.path.join(BASE, info['path'])
    try:
        with open(filepath, 'r') as fh:
            content = fh.read()
    except Exception:
        continue

    folder = info['folder']
    if '03. Atomic' in folder:
        ntype = 'atom'
    elif '04. MOC' in folder:
        ntype = 'moc'
    elif '05. Output' in folder:
        ntype = 'article'
    elif '02. Source' in folder:
        ntype = 'source'
    else:
        ntype = 'system'

    nodes.append({'id': info['name'], 'type': ntype, 'path': info['path']})

    links_found = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    for link in set(links_found):
        target = link.lower()
        if target in file_map:
            edges.append({'source': info['name'], 'target': file_map[target]['name']})

out_path = os.path.join(BASE, 'graph.json')
with open(out_path, 'w') as f:
    json.dump({'nodes': nodes, 'edges': edges}, f, indent=2)

print(f"Generated {out_path}: {len(nodes)} nodes, {len(edges)} edges")
