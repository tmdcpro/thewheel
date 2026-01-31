import requests
from typing import List, Dict
from src.engine.collector import BaseCollector
from src.data.connection import db

class GitHubAdapter(BaseCollector):
    """Collector for GitHub repositories."""

    def __init__(self):
        super().__init__("GitHub")
        self.base_url = "https://api.github.com/search/repositories"

    def search(self, query: str, filters: Dict = None) -> List[Dict]:
        """Search GitHub for repositories matching the query."""
        params = {"q": query, "sort": "stars", "order": "desc"}
        if filters:
            # Example filter: {"language": "python"}
            for key, value in filters.items():
                params["q"] += f" {key}:{value}"

        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            print(f"Error searching GitHub: {response.text}")
            return []

        items = response.json().get("items", [])
        return [self.extract_metadata(item) for item in items]

    def extract_metadata(self, raw_data: Dict) -> Dict:
        """Map raw GitHub repository data to project metadata."""
        return {
            "name": raw_data.get("full_name"),
            "url": raw_data.get("html_url"),
            "description": raw_data.get("description"),
            "stars": raw_data.get("stargazers_count"),
            "author": raw_data.get("owner", {}).get("login"),
            "language": raw_data.get("language"),
            "topics": raw_data.get("topics", [])
        }

    def save_to_graph(self, project_data: Dict):
        """Persist project metadata to Neo4j."""
        query = """
        MERGE (p:Project {url: $url})
        SET p.name = $name, 
            p.stars = $stars, 
            p.description = $description,
            p.primary_language = $language
        
        MERGE (a:Author {username: $author})
        MERGE (a)-[:CREATED]->(p)
        
        WITH p
        UNWIND $topics as topic
        MERGE (t:Topic {name: topic})
        MERGE (p)-[:TAGGED_WITH]->(t)
        """
        
        with db.get_session() as session:
            session.run(query, **project_data)

if __name__ == "__main__":
    # Quick smoke test
    adapter = GitHubAdapter()
    print("Searching GitHub for 'neo4j'...")
    results = adapter.search("neo4j", filters={"language": "python"})
    print(f"Found {len(results)} results.")
    for res in results[:3]:
        print(f"- {res['name']} ({res['stars']} stars)")
