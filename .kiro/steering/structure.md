# Project Structure

## Directory Layout
- `src/`: Core logic
  - `engine/`: Research and analysis logic
  - `data/`: Neo4j drivers and schema definitions
  - `ui/`: D3.js visualization components
- `docs/`: Product and technical documentation
- `.kiro/`: Kiro CLI configuration and prompts
- `.agents/`: Agent implementation plans

## File Naming Conventions
- Python: `snake_case.py`
- Markdown: `kebab-case.md`
- Classes: `PascalCase`

## Module Organization
- Decoupled adapters for different data sources (GitHub, GitLab, PyPI, etc.)
