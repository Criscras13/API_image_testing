@echo off
REM Build the static site (production build)
echo 🏗️  Building static site with Hugo...
docker-compose --profile build up
echo.
echo ✅ Build complete!
echo 📁 Static files generated in site_src/public/
