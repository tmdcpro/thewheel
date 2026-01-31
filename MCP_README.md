# The Wheel - MCP Server

## Installation

1. **Add to your Kiro CLI MCP configuration**:
```json
{
  "mcpServers": {
    "the-wheel": {
      "command": "python3",
      "args": ["/path/to/wheel_mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/thewheel"
      }
    }
  }
}
```

2. **Or install globally**:
```bash
chmod +x wheel_mcp_server.py
sudo ln -s $(pwd)/wheel_mcp_server.py /usr/local/bin/wheel-mcp-server
```

## Usage in Kiro CLI

```bash
# In any Kiro chat session:
> Research the competitive landscape for "web scraping tools"

# The agent will automatically use the MCP tool:
@the-wheel/research_landscape "web scraping tools" --limit 5
```

## What It Provides

- **Competitive Analysis**: Identifies key players in any tech space
- **Market Gaps**: Highlights underserved areas ("Blue Oceans")
- **Strategic Insights**: Relationship mapping between projects
- **Interactive Visualization**: Generates browsable network graphs

## Example Output

```
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
```
