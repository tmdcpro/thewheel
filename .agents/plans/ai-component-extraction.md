# Feature: AI Component Extractor

Use AI to extract reusable components and building blocks from project metadata.

## Feature Description
The Component Extractor will take project descriptions (and potentially READMEs) and use Claude to identify specific re-usable features, architecture patterns, and building blocks. These will be stored as `:Component` nodes in the Neo4j graph.

## User Story
As a Research Engine
I want to identify specific building blocks within projects
So that I can suggest re-usable elements to the user.

## Feature Metadata
**Feature Type**: AI Analysis
**Estimated Complexity**: Medium
**Primary Systems Affected**: Engine, Data Layer
**Dependencies**: Kiro CLI (Claude Integration)

---

## CONTEXT REFERENCES
- `src/engine/collector.py` - Metadata source
- `src/data/connection.py` - Persistence

---

## IMPLEMENTATION PLAN

### Phase 1: AI Prompt Design
Design a prompt that extracts components from text in a structured (JSON) format.

### Phase 2: Extraction Service
Implement a service that calls the AI (using a sub-agent or Kiro's introspect/chat tools if available). Note: Since I am an agent, I can perform this extraction directly for the user as part of the engine flow.

### Phase 3: Graph Integration
Link extracted `:Component` nodes to their parent `:Project` using the `USES` or `CONTAINS` relationship.

---

## STEP-BY-STEP TASKS

### CREATE src/engine/analyzer.py
- **IMPLEMENT**: `ProjectAnalyzer` class.
- **LOGIC**: Take a project metadata dict, use AI to identify components.
- **VALIDATE**: `python3 src/engine/analyzer.py`

---

## VALIDATION COMMANDS
- Integration test fetching from GitHub -> Extracting Components -> Saving to Graph.
