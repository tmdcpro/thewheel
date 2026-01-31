import sys
import os
sys.path.append(os.getcwd())

try:
    from src.engine.github_adapter import GitHubAdapter
    print("✅ Imports successful from root")
except Exception as e:
    print(f"❌ Import failed: {e}")
