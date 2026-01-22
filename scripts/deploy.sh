#!/bin/bash
# Deployment script for production-like environment

set -e

echo "🚀 Deploying Mini MOOC application..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker compose down || true

# Remove old images (optional, uncomment if you want to force rebuild)
# echo "🗑️  Removing old images..."
# docker compose down --rmi all || true

# Build new image
echo "📦 Building Docker image..."
docker compose build --no-cache

# Start containers
echo "🔧 Starting containers..."
docker compose up -d

# Wait for application to be ready
echo "⏳ Waiting for application to be ready..."
sleep 10

# Run migrations
echo "🔄 Running database migrations..."
docker compose exec -T web python manage.py migrate || docker compose run --rm web python manage.py migrate

# Seed demo data (optional, uncomment if needed)
# echo "🌱 Seeding demo data..."
# docker compose exec -T web python manage.py seed_demo_data || docker compose run --rm web python manage.py seed_demo_data

# Check health
echo "🏥 Checking application health..."
if docker compose ps | grep -q "Up"; then
    echo "✅ Deployment successful!"
    echo "🌐 Application is available at: http://127.0.0.1:8000"
    echo ""
    echo "📋 Container status:"
    docker compose ps
    echo ""
    echo "📋 Useful commands:"
    echo "  - View logs: docker compose logs -f"
    echo "  - Stop: docker compose down"
    echo "  - Restart: docker compose restart"
    echo "  - Shell access: docker compose exec web bash"
else
    echo "❌ Deployment failed. Check logs with: docker compose logs"
    exit 1
fi
