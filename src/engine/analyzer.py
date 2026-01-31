from typing import List, Dict
import json

class ProjectAnalyzer:
    """Analyzer for project metadata to identify components and building blocks."""

    def __init__(self):
        pass

    def extract_components(self, project_data: Dict) -> List[Dict]:
        """
        Extract reusable components from project description.
        In a production environment, this would call an LLM.
        For the hackathon, we simulate this with keyword extraction 
        but provide a prompt template for the AI specialist.
        """
        description = project_data.get("description", "").lower()
        components = []

        # Simple heuristic mapping for the prototype
        keywords = {
            "api": {"name": "REST API", "type": "Interface"},
            "database": {"name": "Database Layer", "type": "Storage"},
            "auth": {"name": "Authentication System", "type": "Security"},
            "ui": {"name": "User Interface", "type": "Frontend"},
            "cli": {"name": "Command Line Tool", "type": "Interface"},
            "docker": {"name": "Containerization", "type": "DevOps"},
            "neo4j": {"name": "Graph Database", "type": "Storage"}
        }

        for key, info in keywords.items():
            if key in description:
                components.append(info)

        return components

    def get_ai_extraction_prompt(self, project_data: Dict) -> str:
        """Generate a prompt for the Kiro AI to perform deeper analysis."""
        return f"""
        Analyze the following project and identify its core reusable components, 
        architectural building blocks, and unique features.
        
        Project: {project_data['name']}
        Description: {project_data['description']}
        Topics: {', '.join(project_data['topics'])}
        
        Return the result as a JSON list of objects:
        [{{"name": "Component Name", "type": "Category", "description": "Why it is reusable"}}]
        """

if __name__ == "__main__":
    analyzer = ProjectAnalyzer()
    test_project = {
        "name": "The Wheel",
        "description": "A neo4j based tool with a d3 ui and auth system.",
        "topics": ["graph", "ai"]
    }
    comps = analyzer.extract_components(test_project)
    print(f"Extracted: {comps}")
    print("\nAI Prompt Generation:")
    print(analyzer.get_ai_extraction_prompt(test_project))
