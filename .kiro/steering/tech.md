# Technical Architecture

## Technology Stack
- **Graph Database**: Neo4j (Core knowledge graph for project mapping)
- **Visualization**: D3.js (Interactive landscape and cluster mapping)
- **Version Control**: Jujutsu (jj) (Modern, Git-compatible VCS for rapid branching)
- **Backend Language**: Python 3.11+ (Ideal for research, AI integration, and Neo4j drivers)
- **AI Integration**: Claude-3.5-Sonnet (via Kiro CLI) for similarity analysis and strategic logic
- **Package Manager**: Poetry (Python)

## Architecture Overview
- **Data Collector**: Searches GitHub API and Web (DuckDuckGo/Tavily) for relevant projects.
- **Analysis Engine**: Maps project metadata and code features to Graph nodes.
- **Similarity Scorer**: Calculates edge weights between nodes based on feature overlap.
- **Strategy Advisor**: Generates "Blue Ocean" reports using AI context.

## Development Environment
- Python 3.11+
- Neo4j Desktop or AuraDB (Cloud)
- Jujutsu CLI (`jj`)
- Kiro CLI

## Code Standards
- PEP 8 for Python logic.
- Type hints required for all core services.
- Clean, modular logic for research adapters.
