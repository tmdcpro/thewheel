import argparse
from typing import Dict
from src.engine.github_adapter import GitHubAdapter
from src.engine.analyzer import ProjectAnalyzer
from src.engine.strategy import StrategyAdvisor
from src.data.exporter import export_landscape_to_json
from src.data.connection import db

def run_research(query: str, limit: int = 5):
    print(f"🚀 Starting research for: '{query}'")
    
    # 1. Initialize
    github = GitHubAdapter()
    analyzer = ProjectAnalyzer()
    advisor = StrategyAdvisor()
    
    # 2. Search GitHub
    print(f"🔍 Searching GitHub...")
    projects = github.search(query)
    
    # 3. Process and Persist
    count = 0
    for project in projects[:limit]:
        print(f"📦 Analyzing {project['name']}...")
        
        # Extract components
        components = analyzer.extract_components(project)
        project['components'] = components
        
        # Save to Graph
        github.save_to_graph(project)
        link_components_to_project(project)
        
        count += 1
    
    # 4. Strategy & Export
    print("\n--- Strategy Analysis ---")
    oceans = advisor.identify_blue_oceans()
    for ocean in oceans:
        print(f"🌊 Blue Ocean found in '{ocean['topic']}': Score {ocean['blue_ocean_score']:.2f}")
    
    export_landscape_to_json()
    
    print(f"\n✅ Research complete. Added {count} projects.")
    print("👉 Open 'src/ui/index.html' to visualize the landscape.")

def link_components_to_project(project: Dict):
    """Helper to link extracted components to their project node."""
    query = """
    MATCH (p:Project {url: $url})
    UNWIND $components as component
    MERGE (c:Component {name: component.name})
    SET c.type = component.type
    MERGE (p)-[:USES]->(c)
    """
    with db.get_session() as session:
        session.run(query, url=project['url'], components=project['components'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The Wheel - Research Engine")
    parser.add_argument("query", help="What software/product idea are you researching?")
    parser.add_argument("--limit", type=int, default=5, help="Limit number of projects analyzed")
    parser.add_argument("--mock", action="store_true", help="Run in mock mode without Neo4j")
    
    args = parser.parse_args()
    
    if args.mock:
        db.connect("mock", "", "")
    else:
        # Note: In a real environment, you'd load these from .env
        # db.connect("bolt://localhost:7687", "neo4j", "password")
        pass
    
    try:
        run_research(args.query, args.limit)
    except Exception as e:
        print(f"❌ Error during research: {e}")
        print("Tip: Ensure Neo4j is running and reachable.")
