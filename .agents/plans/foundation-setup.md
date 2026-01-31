# Feature: Foundation Setup

The foundation layer establishes the directory structure, Neo4j schema, and basic connectivity for "The Wheel".

## Feature Description
Set up the core infrastructure required to store and analyze project similarity data. This includes the physical directory structure and the logical graph schema in Neo4j.

## User Story
As a Developer
I want a stable foundation with a graph database and organized folders
So that I can start mapping the software landscape systematically.

## Feature Metadata
**Feature Type**: Foundation
**Estimated Complexity**: Medium
**Primary Systems Affected**: Data Layer, Engine Core
**Dependencies**: Neo4j, Python (pyneo4j)

---

## CONTEXT REFERENCES

### Relevant Codebase Files
- `.kiro/steering/tech.md` - Tech stack definition
- `.kiro/steering/structure.md` - Directory layout definition

### New Files to Create
- `src/data/connection.py` - Neo4j driver initialization
- `src/data/schema.cypher` - Graph schema definition
- `src/engine/collector.py` - Placeholder for data collection logic

---

## IMPLEMENTATION PLAN

### Phase 1: Directory Setup
Establish the project structure defined in `structure.md`.

### Phase 2: Neo4j Schema
Define nodes and relationships in Cypher.
- Nodes: `Project`, `Component`, `Author`, `StrategicNote`
- Relationships: `SIMILAR_TO`, `COMPETES_WITH`, `USES`, `PIVOT_FROM`

### Phase 3: Connectivity
Implement a singleton connection utility for Neo4j.

---

## STEP-BY-STEP TASKS

### CREATE src/data/connection.py
- **IMPLEMENT**: Neo4j singleton connection class using `neo4j` Python driver.
- **IMPORTS**: `from neo4j import GraphDatabase`
- **VALIDATE**: `python3 -c "from src.data.connection import db; print('Connected')"`

### CREATE src/data/schema.cypher
- **IMPLEMENT**: Constraints and indexes for the graph.
- **PATTERN**: Unique constraints on `Project(name)` and `Author(username)`.
- **VALIDATE**: Run via Neo4j Browser or CLI.

### UPDATE src/engine/collector.py
- **IMPLEMENT**: Basic class structure for data collectors.

---

## TESTING STRATEGY
### Unit Tests
- Verify Neo4j connection handling (mocked).
- Verify directory structure exists.

---

## VALIDATION COMMANDS
- `ls -R src/`
- `python3 -m pytest tests/foundation` (once tests are added)
