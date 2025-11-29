#!/bin/bash
# Run the data transformer to fetch fresh API data
echo "🔄 Fetching fresh API data from KnowBe4..."
docker-compose --profile transformer up --build
echo "✅ Data update complete!"
echo "📁 Updated files in site_src/static/"
