# Feature: D3.js Landscape Visualization

Create a prototype for interactive graph visualization.

## Feature Description
An interactive D3.js force-directed graph to visualize projects, components, and their relationships (similarity, usage). This provides the "landscape" view for founders and developers.

## User Story
As a User
I want to see a visual map of similar projects
So that I can identify clusters and "Blue Oceans" (empty spaces).

## Feature Metadata
**Feature Type**: UI/UX
**Estimated Complexity**: Medium
**Primary Systems Affected**: UI Layer
**Dependencies**: D3.js (via CDN)

---

## CONTEXT REFERENCES
- `src/ui/` - Target directory

---

## IMPLEMENTATION PLAN

### Phase 1: HTML Skeleton
Create a clean HTML container with D3.js CDN and a SVG viewport.

### Phase 2: D3 Logic
Implement a force-directed graph:
- Nodes: Projects (circles), Components (rectangles).
- Links: Relationships with varying weights.
- Interactivity: Zoom, Pan, Drag, and Tooltips.

### Phase 3: Data Integration
Design a standard JSON format for the visualization to consume.

---

## STEP-BY-STEP TASKS

### CREATE src/ui/index.html
- **IMPLEMENT**: HTML5 structure with D3 CDN.
- **VALIDATE**: Open in browser (manual).

### CREATE src/ui/viz.js
- **IMPLEMENT**: Force simulation, node/link drawing, and labels.

---

## VALIDATION COMMANDS
- `ls src/ui/`
