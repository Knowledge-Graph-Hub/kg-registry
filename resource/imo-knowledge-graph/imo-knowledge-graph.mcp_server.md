---
category: ProgrammingInterface
connection_url: api.imohealth.com/mcp
description: Model Context Protocol server that exposes the IMO Health Knowledge Graph
  and terminology services as tools for AI assistants and agents. Knowledge Graph
  Access tools include get_relationships, get_hierarchy, and cross_map; additional
  tools cover normalization (normalize_problem, normalize_procedure, normalize_code,
  batch_normalize) and search (search_problem, search_code, get_suggestions). Authentication
  uses a JWT bearer token.
format: http
id: imo-knowledge-graph.mcp_server
is_public: false
name: IMO Health MCP Server
original_source:
- relation_type: prov:hadPrimarySource
  source: imo-knowledge-graph
product_url: https://developer.imohealth.com/mcp-server
warnings:
- Requires IMO Health credentials and a JWT token; the server is not openly accessible.
layout: product_detail
---
