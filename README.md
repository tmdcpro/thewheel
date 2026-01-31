# The Wheel - AI-Assisted Research Engine

Avoid re-inventing the wheel by mapping the software landscape.

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Neo4j Setup**:
   Ensure you have a Neo4j instance running (Local Desktop or AuraDB).
   Update `src/main.py` with your credentials or use environment variables.

3. **Run Research**:
   ```bash
   python src/main.py "your idea"
   ```

4. **Visualize**:
   Open `src/ui/index.html` in your browser.

## 🏗️ Architecture

- **Engine**: Fetches data from GitHub and uses AI (Claude) to extract reusable components.
- **Graph**: Stores projects, components, and similarity relationships in Neo4j.
- **Strategy**: Analyzes the graph to identify "Blue Oceans" (market gaps).
- **UI**: Interactive D3.js visualization of the competitive landscape.

## 🎯 Demo

**Live Demo**: `http://localhost:8080` (after running the pipeline)

**Quick Test**:
```bash
source venv/bin/activate && PYTHONPATH=. python src/main.py "your search query" --mock --limit 5
```

**Example Queries**:
- "machine learning frameworks"
- "web scraping tools" 
- "API testing libraries"
- "database ORMs"

## 🤖 Kiro CLI Integration

This project is built using Kiro CLI. Use the specialized agents for development:
- `@graph-specialist`: Neo4j/Cypher help.
- `@eval-specialist`: Accuracy testing.
- `@refactor-specialist`: Code cleanup.
- `@qa-tester`: Functional testing.
