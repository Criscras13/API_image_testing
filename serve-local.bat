@echo off
REM Run Hugo server for local testing
echo 🚀 Starting Hugo development server...
echo 📡 Site will be available at: http://localhost:1313
echo Press Ctrl+C to stop the server
echo.
docker-compose --profile hugo up
echo.
echo 🛑 Hugo server stopped
