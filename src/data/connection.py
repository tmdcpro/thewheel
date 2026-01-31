from neo4j import GraphDatabase
import os
from typing import Optional

class Neo4jConnection:
    """Singleton Neo4j connection handler."""
    _instance: Optional['Neo4jConnection'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Neo4jConnection, cls).__new__(cls)
            cls._instance._driver = None
            cls._instance.mock_mode = False
            cls._instance.mock_storage = {"nodes": [], "links": []}
        return cls._instance

    def connect(self, uri: str, user: str, password: str):
        if uri == "mock":
            self.mock_mode = True
            print("🛠️ Neo4j Mock Mode enabled.")
            return
        if not self._driver:
            self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_session(self):
        if self.mock_mode:
            return MockSession(self.mock_storage)
        if not self._driver:
            raise ConnectionError("Driver not initialized. Call connect() first.")
        return self._driver.session()

class MockSession:
    """Mock session for testing without a real Neo4j instance."""
    def __init__(self, storage):
        self.storage = storage

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def run(self, query, **kwargs):
        # Store Nodes
        if "MERGE (p:Project" in query or "MERGE (c:Component" in query:
            name = kwargs.get("name") or kwargs.get("author") or (kwargs.get("components")[0]['name'] if kwargs.get("components") else None)
            if name and not any(n['name'] == name for n in self.storage["nodes"]):
                node_id = len(self.storage["nodes"]) + 1
                node_type = "Project" if "p:Project" in query else "Component"
                self.storage["nodes"].append({"id": node_id, "name": name, "type": node_type, "url": kwargs.get("url")})
        
        # Store Links (Simple heuristic for USES/CREATED)
        if "-[:USES]->" in query or "-[:CREATED]->" in query:
            # We assume for the mock that the last added project connects to the last added components
            if len(self.storage["nodes"]) > 1:
                source = self.storage["nodes"][-2]["id"]
                target = self.storage["nodes"][-1]["id"]
                self.storage["links"].append({"source": source, "target": target})
        
        return MockResult(self.storage)

class MockResult:
    def __init__(self, storage):
        self.storage = storage
    def single(self):
        return self.storage
    def __iter__(self):
        return iter([{"topic": "Mock Topic", "blue_ocean_score": 0.85}])

# Global instance
db = Neo4jConnection()
