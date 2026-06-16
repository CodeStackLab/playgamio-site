# Graph Report - playgamio  (2026-06-05)

## Corpus Check
- 3 files · ~1,668 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 104 nodes · 100 edges · 15 communities (10 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1e27506b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]

## God Nodes (most connected - your core abstractions)
1. `What You Must Do When Invoked` - 11 edges
2. `/graphify` - 10 edges
3. `graphify reference: extra exports and benchmark` - 7 edges
4. `init()` - 6 edges
5. `graphify reference: query, path, explain` - 5 edges
6. `fetchGames()` - 4 edges
7. `Step 3 - Extract entities and relationships` - 4 edges
8. `renderGames()` - 3 edges
9. `renderComingSoon()` - 3 edges
10. `PlayGamio` - 3 edges

## Surprising Connections (you probably didn't know these)
- `init()` --calls--> `renderComingSoon()`  [EXTRACTED]
  html/app.js → html/app.js  _Bridges community 4 → community 14_

## Import Cycles
- None detected.

## Communities (15 total, 5 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (28): AVAILABLE_GAMES, closeMapBtn, closeModal, closeSignin, comingSoonGrid, comingSoonSection, featuredStrip, fullscreenBtn (+20 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (14): Part A - Structural extraction for code files, Part B - Semantic extraction (parallel subagents), Part C - Merge AST + semantic into final extraction, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths), Step 1 - Ensure graphify is installed, Step 2.5 - Video and audio (only if video files detected), Step 2 - Detect files, Step 3 - Extract entities and relationships (+6 more)

### Community 2 - "Community 2"
Cohesion: 0.20
Nodes (9): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Usage (+1 more)

### Community 3 - "Community 3"
Cohesion: 0.25
Nodes (7): graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag), Step 7d - MCP server (only if --mcp flag), Step 8 - Token reduction benchmark (only if total_words > 5000)

### Community 4 - "Community 4"
Cohesion: 0.40
Nodes (6): fetchGames(), init(), initGameMap(), renderGames(), renderGenres(), setupEventListeners()

### Community 5 - "Community 5"
Cohesion: 0.33
Nodes (5): For /graphify explain, For /graphify path, graphify reference: query, path, explain, Step 0 — Constrained query expansion (REQUIRED before traversal), Step 1 — Traversal

### Community 6 - "Community 6"
Cohesion: 0.50
Nodes (3): For /graphify add, For --watch, graphify reference: add a URL and watch a folder

### Community 7 - "Community 7"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 8 - "Community 8"
Cohesion: 0.50
Nodes (3): For --cluster-only, For --update (incremental re-extraction), graphify reference: incremental update and cluster-only

### Community 9 - "Community 9"
Cohesion: 0.50
Nodes (3): Live Site, PlayGamio, Structure

## Knowledge Gaps
- **71 isolated node(s):** `genreBar`, `gamesGrid`, `comingSoonGrid`, `featuredStrip`, `gameCountEl` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `What You Must Do When Invoked` connect `Community 1` to `Community 2`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Why does `/graphify` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **What connects `genreBar`, `gamesGrid`, `comingSoonGrid` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.06451612903225806 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._