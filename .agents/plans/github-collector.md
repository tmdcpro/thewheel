# Feature: GitHub Data Collector

Implement the first research adapter to fetch project data from GitHub.

## Feature Description
The GitHub Collector will search GitHub for repositories matching specific keywords and map them to our Neo4j Knowledge Graph. This is the primary data source for "The Wheel".

## User Story
As a Research Engine
I want to fetch repository data from GitHub
So that I can identify existing projects and their components.

## Feature Metadata
**Feature Type**: Data Integration
**Estimated Complexity**: Medium
**Primary Systems Affected**: Engine, Data Layer
**Dependencies**: `requests` or `PyGithub` (prefer `requests` for lightweight search), Neo4j

---

## CONTEXT REFERENCES

### Relevant Codebase Files
- `src/engine/collector.py` - Base class to inherit from
- `src/data/connection.py` - For graph persistence

### New Files to Create
- `src/engine/github_adapter.py` - GitHub specific implementation
- `tests/engine/test_github_adapter.py` - Unit tests for parsing

---

## IMPLEMENTATION PLAN

### Phase 1: Adapter Logic
Inherit from `BaseCollector` and implement GitHub API search.

### Phase 2: Graph Mapping
Map GitHub repository objects to:
- `:Project` (name, url, stars, description)
- `:Author` (login, type)
- `:Component` (inferred from languages/topics)

### Phase 3: Persistence
Add logic to upsert these nodes into Neo4j.

---

## STEP-BY-STEP TASKS

### CREATE src/engine/github_adapter.py
- **IMPLEMENT**: `GitHubAdapter` class. Use GitHub Search API (`https://api.github.com/search/repositories`).
- **PATTERN**: Follow `BaseCollector` interface.
- **VALIDATE**: `python3 -c "from src.engine.github_adapter import GitHubAdapter; print('Imported')"`

### UPDATE src/engine/github_adapter.py (Persistence)
- **IMPLEMENT**: `save_to_graph` method using Cypher `MERGE` to avoid duplicates.
- **QUERY**: 
  ```cypher
  MERGE (p:Project {url: $url})
  SET p.name = $name, p.stars = $stars, p.description = $description
  MERGE (a:Author {username: $author_name})
  MERGE (a)-[:CREATED]->(p)
  ```

---

## VALIDATION COMMANDS
- `python3 src/engine/github_adapter.py` (with a test query)
