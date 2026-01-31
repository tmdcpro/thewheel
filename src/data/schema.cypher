// The Wheel: Neo4j Schema Constraints & Indexes

// Project Constraints
CREATE CONSTRAINT project_name_unique IF NOT EXISTS
FOR (p:Project) REQUIRE p.name IS UNIQUE;

// Author Constraints
CREATE CONSTRAINT author_username_unique IF NOT EXISTS
FOR (a:Author) REQUIRE a.username IS UNIQUE;

// Component Constraints
CREATE CONSTRAINT component_id_unique IF NOT EXISTS
FOR (c:Component) REQUIRE c.id IS UNIQUE;

// Indexes for Similarity Queries
CREATE INDEX project_description_index IF NOT EXISTS
FOR (p:Project) ON (p.description);

CREATE INDEX component_type_index IF NOT EXISTS
FOR (c:Component) ON (c.type);

// Relationships Summary
// (Project)-[:SIMILAR_TO {score: float}]->(Project)
// (Project)-[:USES]->(Component)
// (Project)-[:COMPETES_WITH]->(Project)
// (Author)-[:CREATED]->(Project)
