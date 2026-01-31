#!/bin/bash
# Test script for The Wheel MCP Server

echo "🧪 Testing The Wheel MCP Server..."

# Test 1: Tools list
echo "📋 Test 1: Requesting available tools..."
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}' | PYTHONPATH=. python3 wheel_mcp_server.py

echo -e "\n"

# Test 2: Research call
echo "🔍 Test 2: Research landscape for 'web frameworks'..."
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "research_landscape", "arguments": {"query": "web frameworks", "limit": 3}}}' | PYTHONPATH=. python3 wheel_mcp_server.py

echo -e "\n✅ MCP Server test complete!"
