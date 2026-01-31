import json
from src.data.connection import db

def export_landscape_to_json(output_path: str = "src/ui/data.js"):
    """
    Queries Neo4j and exports the graph to a format compatible with D3.js.
    Uses a .js file to bypass browser CORS for local file opening.
    """
    query = """
    MATCH (n)
    OPTIONAL MATCH (n)-[r]->(m)
    RETURN collect(distinct {id: id(n), name: n.name, type: labels(n)[0], url: n.url}) as nodes,
           collect(distinct {source: id(n), target: id(m), type: type(r)}) as links
    """
    
    print(f"📊 Exporting Neo4j data to {output_path}...")
    
    with db.get_session() as session:
        result = session.run(query).single()
        
        # Filter out empty targets in links
        links = [l for l in result['links'] if l['target'] is not None]
        
        data = {
            "nodes": result['nodes'],
            "links": links
        }
        
        with open(output_path, 'w') as f:
            f.write(f"const graphData = {json.dumps(data, indent=2)};")
            
    print(f"✅ Export complete. Found {len(data['nodes'])} nodes and {len(data['links'])} links.")

if __name__ == "__main__":
    # Smoke test
    # db.connect(...)
    try:
        export_landscape_to_json()
    except Exception as e:
        print(f"❌ Export failed: {e}")
