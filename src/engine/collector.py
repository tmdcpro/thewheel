from typing import List, Dict

class BaseCollector:
    """Base class for all data source collectors (GitHub, Web, etc.)."""
    
    def __init__(self, source_name: str):
        self.source_name = source_name

    def search(self, query: str, filters: Dict = None) -> List[Dict]:
        """Search the source for projects/components."""
        raise NotImplementedError("Subclasses must implement search()")

    def extract_metadata(self, raw_data: Dict) -> Dict:
        """Parse raw response into standardized project format."""
        raise NotImplementedError("Subclasses must implement extract_metadata()")
