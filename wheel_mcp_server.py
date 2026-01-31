#!/usr/bin/env python3
"""
The Wheel - MCP Server
Provides competitive landscape research as an MCP tool for AI agents.
"""

import json
import sys
from typing import Any, Dict, List
from src.main import run_research
from src.data.connection import db

class WheelMCPServer:
    def __init__(self):
        self.name = "the-wheel"
        self.version = "1.0.0"
        
    def get_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "research_landscape",
                "description": "Research competitive landscape for a technology/product area",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Technology or product area to research (e.g., 'machine learning frameworks')"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Number of projects to analyze (default: 5)",
                            "default": 5
                        }
                    },
                    "required": ["query"]
                }
            }
        ]
    
    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if name == "research_landscape":
            query = arguments.get("query", "")
            limit = arguments.get("limit", 5)
            
            try:
                # Enable mock mode for MCP usage
                db.connect("mock", "", "")
                
                # Run the research pipeline
                run_research(query, limit)
                
                # Get the results from mock storage
                with db.get_session() as session:
                    # Access mock storage directly
                    nodes = session.storage["nodes"]
                    links = session.storage["links"]
                
                # Format response
                projects = [n for n in nodes if n.get("type") == "Project"]
                
                response = f"""# Competitive Landscape: {query}

## 📊 Research Results
- **Projects Found**: {len(projects)}
- **Total Nodes**: {len(nodes)}
- **Relationships**: {len(links)}

## 🏢 Key Projects
"""
                for project in projects[:5]:
                    response += f"- **{project['name']}**: {project.get('url', 'No URL')}\n"
                
                response += f"""
## 🎯 Strategic Insights
- Dense clusters indicate saturated markets
- Isolated projects may represent unique approaches
- Missing connections suggest partnership opportunities

## 📈 Visualization
Run this command to see the interactive graph:
```bash
python src/main.py "{query}" --mock --limit {limit}
```
Then open `standalone_demo.html` in your browser.
"""
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": response
                        }
                    ]
                }
                
            except Exception as e:
                return {
                    "content": [
                        {
                            "type": "text", 
                            "text": f"❌ Research failed: {str(e)}"
                        }
                    ],
                    "isError": True
                }
        
        return {"content": [{"type": "text", "text": "Unknown tool"}], "isError": True}

def main():
    server = WheelMCPServer()
    
    # Simple MCP protocol handler
    for line in sys.stdin:
        try:
            request = json.loads(line.strip())
            
            if request.get("method") == "tools/list":
                response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "result": {"tools": server.get_tools()}
                }
            elif request.get("method") == "tools/call":
                params = request.get("params", {})
                result = server.call_tool(params.get("name"), params.get("arguments", {}))
                response = {
                    "jsonrpc": "2.0", 
                    "id": request.get("id"),
                    "result": result
                }
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "error": {"code": -32601, "message": "Method not found"}
                }
            
            print(json.dumps(response))
            sys.stdout.flush()
            
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id") if 'request' in locals() else None,
                "error": {"code": -32603, "message": str(e)}
            }
            print(json.dumps(error_response))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
