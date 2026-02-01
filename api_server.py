#!/usr/bin/env python3
"""
Simple Flask API server for The Wheel
Provides live GitHub search functionality to the web interface
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from engine.github_adapter import GitHubAdapter
from engine.analyzer import ProjectAnalyzer
from data.connection import db

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Initialize components
github_adapter = GitHubAdapter()
analyzer = ProjectAnalyzer()

@app.route('/api/search', methods=['POST'])
def search_projects():
    """Search for projects using live GitHub API"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        filters = data.get('filters', {})
        
        if not query:
            return jsonify({'error': 'Query is required'}), 400
        
        # Enable mock mode for development
        db.connect("mock", "", "")
        
        # Search GitHub
        projects = github_adapter.search(query, filters)
        
        # Process projects and extract components
        nodes = []
        links = []
        node_id = 1
        
        for project in projects:
            # Add project node
            nodes.append({
                'id': node_id,
                'name': project['name'],
                'type': 'Project',
                'url': project['url'],
                'description': project['description'],
                'stars': project['stars'],
                'language': project['language']
            })
            project_id = node_id
            node_id += 1
            
            # Extract and add components
            components = analyzer.extract_components(project)
            for component in components:
                # Check if component already exists
                existing_component = next((n for n in nodes if n['name'] == component['name'] and n['type'] == 'Component'), None)
                
                if existing_component:
                    # Link to existing component
                    links.append({
                        'source': project_id,
                        'target': existing_component['id']
                    })
                else:
                    # Create new component
                    nodes.append({
                        'id': node_id,
                        'name': component['name'],
                        'type': 'Component',
                        'category': component['type']
                    })
                    links.append({
                        'source': project_id,
                        'target': node_id
                    })
                    node_id += 1
        
        # Add some inter-project relationships for better visualization
        for i in range(len(projects) - 1):
            if i < len(nodes) - 1:
                links.append({
                    'source': i + 1,
                    'target': i + 2
                })
        
        return jsonify({
            'nodes': nodes,
            'links': links,
            'query': query,
            'total_projects': len(projects)
        })
        
    except Exception as e:
        print(f"API Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'The Wheel API'})

if __name__ == '__main__':
    print("🚀 Starting The Wheel API server...")
    print("📡 Live GitHub search enabled")
    print("🌐 Access at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
