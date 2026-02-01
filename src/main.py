import argparse
import sys
import os
from typing import Dict

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.engine.github_adapter import GitHubAdapter
from src.engine.analyzer import ProjectAnalyzer
from src.engine.strategy import StrategyAdvisor
from src.data.exporter import export_landscape_to_json
from src.data.connection import db

def run_research(query: str, limit: int = 5, filters: Dict = None):
    print(f"🚀 Starting research for: '{query}'")
    if filters:
        print(f"🔧 Applying filters: {filters}")
    
    # 1. Initialize
    github = GitHubAdapter()
    analyzer = ProjectAnalyzer()
    advisor = StrategyAdvisor()
    
    # 2. Search GitHub with filters
    print(f"🔍 Searching GitHub...")
    projects = github.search(query, filters)
    
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
    print("👉 Open 'standalone_demo.html' to visualize and search the landscape.")

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
    parser = argparse.ArgumentParser(description="The Wheel - Interactive Research Engine")
    parser.add_argument("query", help="What software/product idea are you researching?")
    parser.add_argument("--limit", type=int, default=5, help="Limit number of projects analyzed")
    parser.add_argument("--mock", action="store_true", help="Run in mock mode without Neo4j")
    
    # Filter arguments
    parser.add_argument("--language", help="Filter by programming language")
    parser.add_argument("--min-stars", type=int, help="Minimum number of stars")
    parser.add_argument("--updated", choices=['week', 'month', 'year'], help="Recently updated filter")
    parser.add_argument("--topic", help="Filter by GitHub topic")
    
    args = parser.parse_args()
    
    # Build filters dictionary
    filters = {}
    if args.language:
        filters['language'] = args.language
    if args.min_stars:
        filters['stars'] = f">={args.min_stars}"
    if args.updated:
        filters['pushed'] = f">={args.updated}"
    if args.topic:
        filters['topic'] = args.topic
    
    if args.mock:
        db.connect("mock", "", "")
    else:
        # Note: In a real environment, you'd load these from .env
        # db.connect("bolt://localhost:7687", "neo4j", "password")
        pass
    
    try:
        run_research(args.query, args.limit, filters if filters else None)
    except Exception as e:
        print(f"❌ Error during research: {e}")
        print("Tip: Ensure Neo4j is running and reachable.")
