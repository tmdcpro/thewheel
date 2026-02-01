#!/bin/bash
# The Wheel - Live Demo Startup Script

echo "🎯 The Wheel - Live GitHub Search Demo"
echo "======================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run:"
    echo "   python3 -m venv venv"
    echo "   source venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Start API server in background
echo "🚀 Starting API server..."
python3 api_server.py &
API_PID=$!

# Wait for API to start
echo "⏳ Waiting for API server to start..."
sleep 3

# Check if API is running
if curl -s http://localhost:5000/api/health > /dev/null; then
    echo "✅ API server running at http://localhost:5000"
else
    echo "⚠️ API server may not be ready yet"
fi

# Start simple HTTP server for frontend
echo "🌐 Starting frontend server..."
python3 -m http.server 8080 &
HTTP_PID=$!

echo ""
echo "🎉 The Wheel is now running!"
echo "================================"
echo "🔗 Frontend: http://localhost:8080/standalone_demo.html"
echo "🔗 API: http://localhost:5000"
echo ""
echo "Features available:"
echo "  ✅ Live GitHub API search"
echo "  ✅ Advanced filtering"
echo "  ✅ Blue Ocean analysis"
echo "  ✅ Interactive visualization"
echo "  ✅ Export functionality"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for user interrupt
trap "echo ''; echo '🛑 Stopping servers...'; kill $API_PID $HTTP_PID 2>/dev/null; echo '✅ Servers stopped'; exit 0" INT

# Keep script running
wait
