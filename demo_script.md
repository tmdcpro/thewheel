# The Wheel - Demo Script

## 🎯 **Value Proposition** (30 seconds)
"The Wheel helps developers and founders avoid re-inventing existing software by mapping the competitive landscape and identifying reusable components."

## 🚀 **Live Demo** (90 seconds)

### 1. Research Query
```bash
source venv/bin/activate && PYTHONPATH=. python src/main.py "AI chatbot frameworks" --mock --limit 4
```

**What's happening:**
- Searches GitHub for relevant projects
- Extracts reusable components using AI analysis
- Maps relationships in a graph database
- Identifies market gaps ("Blue Oceans")

### 2. Visualization
Open: `http://localhost:8080`

**Show:**
- Interactive node graph of competing projects
- Click nodes to open GitHub repositories
- Hover for component details
- Network shows how projects relate

### 3. Strategic Insights
**Point out:**
- Dense clusters = saturated markets
- Isolated nodes = unique approaches
- Missing connections = opportunities

## 🏗️ **Technical Architecture** (30 seconds)
- **Backend**: Python + Neo4j graph database
- **AI Integration**: Component extraction via LLM analysis
- **Frontend**: D3.js interactive visualization
- **Data Sources**: GitHub API (extensible to PyPI, NPM, etc.)

## 🎯 **Use Cases** (30 seconds)
1. **Founders**: Validate market positioning before building
2. **Developers**: Find existing libraries to reuse
3. **Investors**: Analyze competitive landscapes
4. **Researchers**: Map technology ecosystems

## 🚀 **Next Steps**
- Real Neo4j deployment
- Multiple data sources (PyPI, NPM, Docker Hub)
- Advanced AI analysis for deeper insights
- Team collaboration features

---
**Total Time: 3 minutes**
