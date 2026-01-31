# The Wheel - AI-Assisted Research Engine

> **"Don't reinvent the wheel"** - Map the software landscape and discover reusable components before you build.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Neo4j](https://img.shields.io/badge/database-Neo4j-green.svg)](https://neo4j.com/)
[![Kiro CLI](https://img.shields.io/badge/integration-Kiro%20CLI-purple.svg)](https://kiro.dev/)

## 🎯 Overview

**The Wheel** is an AI-powered competitive landscape research engine that helps developers, founders, and product managers avoid reinventing existing software by mapping the technology ecosystem and identifying reusable components.

### Key Features

- 🔍 **Intelligent Research**: Searches GitHub and analyzes project metadata using AI
- 🕸️ **Graph Relationships**: Maps connections between projects, components, and technologies
- 📊 **Interactive Visualization**: D3.js-powered network graphs for exploring landscapes
- 🌊 **Blue Ocean Detection**: Identifies market gaps and underserved opportunities
- 🤖 **MCP Integration**: Works seamlessly with Kiro CLI and other AI agents
- ⚡ **Mock Mode**: Demo-ready without external database dependencies

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Git
- Virtual environment support

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tmdcpro/thewheel.git
   cd thewheel
   ```

2. **Set up virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Basic Usage

**Research a technology landscape**:
```bash
source venv/bin/activate
PYTHONPATH=. python src/main.py "machine learning frameworks" --mock --limit 5
```

**View interactive visualization**:
```bash
# Open standalone_demo.html in your browser
open standalone_demo.html
```

## 🎯 Demo

**Live Visualization**: Open `standalone_demo.html` in your browser after running a research query.

**Example Queries**:
- `"machine learning frameworks"`
- `"web scraping tools"` 
- `"API testing libraries"`
- `"database ORMs"`
- `"authentication systems"`

**What You'll See**:
- Interactive network graph of competing projects
- Click blue nodes to open GitHub repositories
- Drag nodes to explore relationships
- Real-time statistics and insights

## 🏗️ Architecture

### Core Components

- **Research Engine** (`src/engine/`): GitHub API integration and data collection
- **Analysis Pipeline** (`src/engine/analyzer.py`): AI-powered component extraction
- **Graph Database** (`src/data/`): Neo4j for relationship mapping (with mock mode)
- **Visualization** (`src/ui/`): D3.js interactive network graphs
- **MCP Server** (`wheel_mcp_server.py`): Integration with AI agent ecosystems

### Data Flow

```
GitHub API → Component Analysis → Graph Storage → Visualization
     ↓              ↓                 ↓             ↓
  Projects    AI Extraction      Relationships   D3.js Graph
```

## 🤖 MCP Server Integration

**The Wheel** includes a Model Context Protocol (MCP) server for seamless integration with AI agents like Kiro CLI.

### Installation

1. **Add to your Kiro CLI configuration** (`.kiro/settings/mcp.json`):
   ```json
   {
     "mcpServers": {
       "the-wheel": {
         "command": "python3",
         "args": ["./wheel_mcp_server.py"],
         "env": {
           "PYTHONPATH": "."
         }
       }
     }
   }
   ```

2. **Test the integration**:
   ```bash
   ./test_mcp.sh
   ```

### Usage in AI Agents

```bash
# In Kiro CLI or any MCP-compatible agent:
> Research the competitive landscape for "web frameworks"

# The agent automatically uses The Wheel's research capabilities
```

## 📊 Example Output

```markdown
# Competitive Landscape: machine learning frameworks

## 📊 Research Results
- Projects Found: 5
- Total Nodes: 5
- Relationships: 6

## 🏢 Key Projects
- tensorflow/tensorflow: https://github.com/tensorflow/tensorflow
- huggingface/transformers: https://github.com/huggingface/transformers
- josephmisiti/awesome-machine-learning: https://github.com/josephmisiti/awesome-machine-learning

## 🎯 Strategic Insights
- Dense clusters indicate saturated markets
- Isolated projects may represent unique approaches
- Missing connections suggest partnership opportunities
```

## 🛠️ Development

### Project Structure

```
thewheel/
├── src/
│   ├── engine/          # Research and analysis logic
│   │   ├── github_adapter.py    # GitHub API integration
│   │   ├── analyzer.py          # AI component extraction
│   │   └── strategy.py          # Blue ocean analysis
│   ├── data/            # Database and persistence
│   │   ├── connection.py        # Neo4j connection (with mock)
│   │   ├── schema.cypher        # Graph schema
│   │   └── exporter.py          # Data export utilities
│   └── ui/              # Visualization components
│       ├── index.html           # Main visualization page
│       └── viz.js               # D3.js graph logic
├── .kiro/               # Kiro CLI configuration
│   ├── steering/        # Project knowledge
│   ├── prompts/         # Custom commands
│   └── agents/          # Specialized agents
├── wheel_mcp_server.py  # MCP server implementation
├── standalone_demo.html # Self-contained demo
└── requirements.txt     # Python dependencies
```

### Running Tests

```bash
# Test core pipeline
source venv/bin/activate
PYTHONPATH=. python src/main.py "test query" --mock --limit 3

# Test MCP server
./test_mcp.sh

# Test imports
python test_imports.py
```

### Development with Kiro CLI

This project was built using **Kiro CLI** for accelerated development:

- `@prime` - Load comprehensive project context
- `@plan-feature` - Create implementation plans
- `@execute` - Systematic task execution
- `@code-review` - Quality assurance

## 🗺️ Roadmap

### Phase 1: Foundation ✅ (Current)
- Core GitHub research pipeline
- Neo4j graph storage with mock mode
- Interactive D3.js visualization
- MCP server integration

### Phase 2: IDE Integration (2-4 weeks)
- **VSCode Extension**: Right-click research, sidebar panels
- **JetBrains Plugin**: IntelliJ, PyCharm integration
- **Contextual Suggestions**: Inline component recommendations

### Phase 3: Browser Assistant (4-6 weeks)
- **Browser Extension**: GitHub overlay, package manager insights
- **Research Workflow**: Seamless competitive analysis
- **Product Manager Tools**: Market research automation

### Phase 4: CLI & Terminal (6-8 weeks)
- **Standalone CLI**: `wheel research "query"`
- **Shell Integration**: Package installation suggestions
- **Git Hooks**: Dependency analysis automation

### Phase 5: Enterprise Features (8-12 weeks)
- **Team Collaboration**: Slack/Teams bots
- **API Service**: Enterprise research API
- **Knowledge Management**: Organizational intelligence

## 🎯 Use Cases

### For Developers
- **Library Discovery**: Find existing solutions before building
- **Architecture Planning**: Understand technology ecosystems
- **Dependency Analysis**: Evaluate alternatives and competitors

### For Founders
- **Market Validation**: Assess competitive landscapes
- **Technology Decisions**: Choose proven vs. innovative approaches
- **Partnership Opportunities**: Identify collaboration potential

### For Product Managers
- **Competitive Intelligence**: Track market movements
- **Feature Planning**: Avoid duplicating existing solutions
- **Strategic Positioning**: Find market gaps and opportunities

### For Researchers
- **Technology Mapping**: Understand domain relationships
- **Trend Analysis**: Track ecosystem evolution
- **Academic Research**: Systematic literature reviews

## 🤝 Contributing

We welcome contributions! This project demonstrates:

- **Modern Python Architecture**: Clean, modular design
- **Graph Database Integration**: Neo4j relationship modeling
- **AI-Powered Analysis**: Component extraction and insights
- **Interactive Visualization**: D3.js network graphs
- **MCP Protocol**: AI agent ecosystem integration

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Follow the existing code style
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Kiro CLI**: Development acceleration and AI integration
- **Neo4j**: Graph database technology
- **D3.js**: Interactive visualization framework
- **GitHub API**: Open source project data
- **MCP Protocol**: AI agent interoperability

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/tmdcpro/thewheel/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tmdcpro/thewheel/discussions)
- **Documentation**: See `DEVLOG.md` for development history

---

**Built with ❤️ using Kiro CLI for the Dynamous Hackathon**

*"The best way to predict the future is to map the present."*
