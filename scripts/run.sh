#!/bin/bash
# Run script for local development with Docker

set -e

echo "🚀 Starting Mini MOOC application..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Build and start containers
echo "📦 Building Docker image..."
docker compose build

echo "🔧 Starting containers..."
docker compose up -d

echo "⏳ Waiting for application to be ready..."
sleep 5

# Check if container is running
if docker compose ps | grep -q "Up"; then
    echo "✅ Application is running!"
    echo "🌐 Access the application at: http://127.0.0.1:8000"
    echo ""
    echo "📋 Useful commands:"
    echo "  - View logs: docker compose logs -f"
    echo "  - Stop: docker compose down"
    echo "  - Restart: docker compose restart"
    echo ""
    echo "🔍 Showing logs (Ctrl+C to exit)..."
    docker compose logs -f
else
    echo "❌ Failed to start application. Check logs with: docker compose logs"
    exit 1
fi
