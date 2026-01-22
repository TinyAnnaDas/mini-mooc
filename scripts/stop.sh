#!/bin/bash
# Stop script for Docker containers

set -e

echo "🛑 Stopping Mini MOOC application..."

docker compose down

echo "✅ Application stopped."
