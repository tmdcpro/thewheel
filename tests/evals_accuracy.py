import pytest
from src.engine.analyzer import ProjectAnalyzer

def test_component_extraction_accuracy():
    """Eval: Verify if the analyzer correctly identifies 'Neo4j' as a Graph Database."""
    analyzer = ProjectAnalyzer()
    
    benchmark_data = {
        "name": "Graph Master",
        "description": "A tool that uses neo4j for storage and d3 for viz.",
        "topics": []
    }
    
    components = analyzer.extract_components(benchmark_data)
    component_names = [c['name'] for c in components]
    
    assert "Graph Database" in component_names
    assert "User Interface" in component_names
    
def test_empty_description_handling():
    """Eval: Ensure the analyzer handles empty data without crashing."""
    analyzer = ProjectAnalyzer()
    components = analyzer.extract_components({"description": ""})
    assert components == []

if __name__ == "__main__":
    print("Running Evals...")
    pytest.main([__file__])
