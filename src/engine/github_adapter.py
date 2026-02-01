import requests
from typing import List, Dict
from src.engine.collector import BaseCollector
from src.data.connection import db

class GitHubAdapter(BaseCollector):
    """Collector for GitHub repositories with live API integration."""

    def __init__(self, api_token: str = None):
        super().__init__("GitHub")
        self.base_url = "https://api.github.com/search/repositories"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "TheWheel-Research-Engine/1.0"
        }
        if api_token:
            self.headers["Authorization"] = f"token {api_token}"

    def search(self, query: str, filters: Dict = None) -> List[Dict]:
        """Search GitHub for repositories matching the query."""
        # Build search query
        search_query = query
        
        if filters:
            if filters.get('language'):
                search_query += f" language:{filters['language']}"
            if filters.get('stars'):
                search_query += f" stars:{filters['stars']}"
            if filters.get('pushed'):
                search_query += f" pushed:{filters['pushed']}"
            if filters.get('topic'):
                search_query += f" topic:{filters['topic']}"
        
        params = {
            "q": search_query,
            "sort": "stars",
            "order": "desc",
            "per_page": min(int(filters.get('limit', 10)) if filters else 10, 100)
        }

        try:
            print(f"🔍 Searching GitHub API: {search_query}")
            response = requests.get(self.base_url, params=params, headers=self.headers, timeout=10)
            
            if response.status_code == 403:
                print("⚠️ GitHub API rate limit exceeded. Using cached/mock data.")
                return self._get_mock_data(query, filters)
            elif response.status_code != 200:
                print(f"⚠️ GitHub API error {response.status_code}: {response.text}")
                return self._get_mock_data(query, filters)

            data = response.json()
            items = data.get("items", [])
            
            print(f"✅ Found {len(items)} repositories from GitHub API")
            return [self.extract_metadata(item) for item in items]
            
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Network error accessing GitHub API: {e}")
            return self._get_mock_data(query, filters)
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            return self._get_mock_data(query, filters)

    def _get_mock_data(self, query: str, filters: Dict = None) -> List[Dict]:
        """Fallback mock data when API is unavailable."""
        print("🛠️ Using mock data as fallback")
        
        mock_projects = [
            {"name": "facebook/react", "url": "https://github.com/facebook/react", "description": "A declarative, efficient, and flexible JavaScript library for building user interfaces.", "stars": 220000, "author": "facebook", "language": "javascript", "topics": ["javascript", "react", "frontend"]},
            {"name": "vuejs/vue", "url": "https://github.com/vuejs/vue", "description": "Vue.js is a progressive, incrementally-adoptable JavaScript framework for building UI on the web.", "stars": 207000, "author": "vuejs", "language": "javascript", "topics": ["javascript", "vue", "frontend"]},
            {"name": "tensorflow/tensorflow", "url": "https://github.com/tensorflow/tensorflow", "description": "An Open Source Machine Learning Framework for Everyone", "stars": 185000, "author": "tensorflow", "language": "python", "topics": ["machine-learning", "tensorflow", "python"]},
            {"name": "pytorch/pytorch", "url": "https://github.com/pytorch/pytorch", "description": "Tensors and Dynamic neural networks in Python with strong GPU acceleration", "stars": 78000, "author": "pytorch", "language": "python", "topics": ["machine-learning", "pytorch", "python"]},
            {"name": "django/django", "url": "https://github.com/django/django", "description": "The Web framework for perfectionists with deadlines.", "stars": 76000, "author": "django", "language": "python", "topics": ["web", "django", "python"]},
            {"name": "expressjs/express", "url": "https://github.com/expressjs/express", "description": "Fast, unopinionated, minimalist web framework for node.", "stars": 64000, "author": "expressjs", "language": "javascript", "topics": ["web", "express", "nodejs"]},
            {"name": "gin-gonic/gin", "url": "https://github.com/gin-gonic/gin", "description": "Gin is a HTTP web framework written in Go (Golang).", "stars": 75000, "author": "gin-gonic", "language": "go", "topics": ["web", "gin", "golang"]},
            {"name": "scikit-learn/scikit-learn", "url": "https://github.com/scikit-learn/scikit-learn", "description": "scikit-learn: machine learning in Python", "stars": 58000, "author": "scikit-learn", "language": "python", "topics": ["machine-learning", "python", "scikit-learn"]}
        ]

        # Filter mock data based on query and filters
        filtered = []
        for project in mock_projects:
            # Check if query matches
            if (query.lower() in project['name'].lower() or 
                query.lower() in project['description'].lower() or
                any(query.lower() in topic for topic in project['topics'])):
                
                # Apply filters
                if filters:
                    if filters.get('language') and project['language'] != filters['language']:
                        continue
                    if filters.get('stars'):
                        min_stars = int(filters['stars'].replace('>=', '').replace('+', ''))
                        if project['stars'] < min_stars:
                            continue
                
                filtered.append(self.extract_metadata(project))
        
        limit = int(filters.get('limit', 5)) if filters else 5
        return filtered[:limit]

    def extract_metadata(self, raw_data: Dict) -> Dict:
        """Map raw GitHub repository data to project metadata."""
        return {
            "name": raw_data.get("full_name") or raw_data.get("name"),
            "url": raw_data.get("html_url") or raw_data.get("url"),
            "description": raw_data.get("description", "No description available"),
            "stars": raw_data.get("stargazers_count") or raw_data.get("stars", 0),
            "author": raw_data.get("owner", {}).get("login") if raw_data.get("owner") else raw_data.get("author"),
            "language": (raw_data.get("language") or raw_data.get("language", "")).lower(),
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
    # Quick test
    adapter = GitHubAdapter()
    print("Testing live GitHub search...")
    results = adapter.search("web frameworks", {"language": "javascript", "limit": "3"})
    print(f"Found {len(results)} results:")
    for res in results[:3]:
        print(f"- {res['name']} ({res['stars']} stars)")
