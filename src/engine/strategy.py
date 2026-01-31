from src.data.connection import db
from typing import List, Dict

class StrategyAdvisor:
    """Strategy Advisor to identify 'Blue Oceans' and re-use opportunities."""

    def identify_blue_oceans(self) -> List[Dict]:
        """
        Identify areas with many projects but few shared components/standardization.
        (A simple heuristic for 'The Wheel' prototype).
        """
        query = """
        MATCH (p:Project)-[:TAGGED_WITH]->(t:Topic)
        WITH t, count(p) as project_count
        WHERE project_count > 1
        OPTIONAL MATCH (p:Project)-[:TAGGED_WITH]->(t)
        OPTIONAL MATCH (p)-[:USES]->(c:Component)
        WITH t, project_count, count(distinct c) as component_count
        RETURN t.name as topic, 
               project_count, 
               component_count, 
               (project_count * 1.0 / (component_count + 1)) as blue_ocean_score
        ORDER BY blue_ocean_score DESC
        LIMIT 5
        """
        
        print("🔍 Searching for Blue Oceans in the Knowledge Graph...")
        
        with db.get_session() as session:
            results = session.run(query)
            return [dict(r) for r in results]

    def propose_pivots(self, project_name: str) -> str:
        """Propose a pivot strategy based on project similarity."""
        # This would ideally use an LLM with graph context.
        # For the prototype, we return a template.
        return f"Pivot Strategy for {project_name}: Identify components used by competitors and integrate them to achieve feature parity, then focus on a Blue Ocean topic identified by the advisor."

if __name__ == "__main__":
    advisor = StrategyAdvisor()
    # Mock run
    try:
        oceans = advisor.identify_blue_oceans()
        print(f"Top Blue Ocean Opportunities: {oceans}")
    except Exception as e:
        print(f"❌ Strategy analysis failed: {e}")
