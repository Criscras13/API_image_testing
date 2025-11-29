# Docker Documentation for API_testing

## Overview

This project includes Docker support for local development and testing. All components are **independent** and **optional**. The existing GitHub Actions deployment workflow is unchanged.

## Architecture

### Independent Components

1. **Data Transformer** (`Dockerfile.transformer`)
   - Fetches fresh data from the KnowBe4 API
   - Outputs JSON and HTML files to `site_src/static/`
   - Runs independently when you need fresh data

2. **Hugo Builder/Server** (`Dockerfile.hugo`)
   - Builds the static site with Hugo
   - Runs a local development server with auto-reload
   - Runs independently when you want to test locally

3. **GitHub Actions** (unchanged)
   - Continues to handle production deployment
   - No Docker dependencies
   - Works exactly as before

## Quick Start

### Option 1: Helper Scripts (Easiest)

**Update API data:**
```bash
# Linux/Mac
./update-data.sh

# Windows
update-data.bat
```

**Run local Hugo server:**
```bash
# Linux/Mac
./serve-local.sh

# Windows
serve-local.bat

# Then visit: http://localhost:1313
```

**Build static site:**
```bash
# Linux/Mac
./build-site.sh

# Windows
build-site.bat
```

### Option 2: Docker Compose Commands

```bash
# Update API data
docker-compose --profile transformer up

# Run local server (auto-reloads on changes)
docker-compose --profile hugo up

# Build static site (production build)
docker-compose --profile build up

# Rebuild a service with latest changes
docker-compose --profile hugo up --build
```

## Detailed Usage

### Fetching Fresh API Data

The data transformer fetches articles, sections, and categories from the KnowBe4 API and generates both JSON and HTML wrapper files.

```bash
# Using helper script
./update-data.sh  # or update-data.bat on Windows

# Using docker-compose
docker-compose --profile transformer up

# Direct Docker command
docker build -f Dockerfile.transformer -t api-testing-transformer .
docker run -v "${PWD}/site_src/static:/app/site_src/static" api-testing-transformer
```

**What happens:**
1. Container fetches data from `https://support.knowbe4.com/api/v2/`
2. Rewrites URLs to point to your GitHub Pages
3. Generates `.json` files for API clients
4. Generates `.html` files for AI browsing tools
5. Saves everything to `site_src/static/api/v2/help_center/en-us/`

### Running Hugo Development Server

The Hugo server provides a local preview with live reload.

```bash
# Using helper script
./serve-local.sh  # or serve-local.bat on Windows

# Using docker-compose
docker-compose --profile hugo up

# Direct Docker command
docker build -f Dockerfile.hugo -t api-testing-hugo .
docker run -p 1313:1313 -v "${PWD}/site_src:/src" api-testing-hugo
```

**What happens:**
1. Hugo server starts on port 1313
2. Watches for file changes
3. Auto-rebuilds and refreshes browser
4. Site available at http://localhost:1313

**Stop the server:** Press `Ctrl+C`

### Building Static Site (Production)

Build the final static files exactly like GitHub Actions does.

```bash
# Using helper script
./build-site.sh  # or build-site.bat on Windows

# Using docker-compose
docker-compose --profile build up

# Direct Docker command
docker build -f Dockerfile.hugo -t api-testing-hugo .
docker run -v "${PWD}/site_src:/src" -v "${PWD}/public:/src/public" api-testing-hugo --minify
```

**What happens:**
1. Hugo builds the site with minification
2. Outputs to `site_src/public/`
3. Same build process as GitHub Actions

## Typical Workflows

### Workflow 1: Update Data and Test Locally

```bash
# Step 1: Get fresh data from API
./update-data.sh

# Step 2: Start local server
./serve-local.sh

# Step 3: View at http://localhost:1313
# Verify the data looks correct

# Step 4: If satisfied, commit and push
git add site_src/static/
git commit -m "Update API data"
git push origin main

# GitHub Actions will automatically deploy
```

### Workflow 2: Develop Hugo Templates

```bash
# Step 1: Start Hugo server (watches for changes)
./serve-local.sh

# Step 2: Edit files in site_src/
# Hugo will auto-reload in browser

# Step 3: When satisfied, commit changes
git add site_src/
git commit -m "Update site templates"
git push origin main
```

### Workflow 3: Test Production Build

```bash
# Build exactly like GitHub Actions does
./build-site.sh

# Verify output
ls site_src/public/

# Test specific endpoints
cat site_src/public/api/v2/help_center/en-us/articles.json
cat site_src/public/api/v2/help_center/en-us/articles.html
```

## Configuration

### Changing Hugo Version

Edit `Dockerfile.hugo` and change the version tag:

```dockerfile
# Current version
FROM klakegg/hugo:0.120.4-ext-alpine

# Change to different version
FROM klakegg/hugo:0.123.0-ext-alpine
```

Available versions: https://hub.docker.com/r/klakegg/hugo/tags

**Important:** Should match the version in `.github/workflows/hugo.yaml` (currently set to 'latest')

### Changing Python Version

Edit `Dockerfile.transformer` and change the base image:

```dockerfile
# Current version
FROM python:3.11-slim

# Change to different version
FROM python:3.12-slim
```

### Adding Python Dependencies

If you need to add external Python packages:

1. Edit `requirements.txt`:
   ```
   requests==2.31.0
   beautifulsoup4==4.12.0
   ```

2. Update `Dockerfile.transformer`:
   ```dockerfile
   # Add after WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   ```

3. Rebuild:
   ```bash
   docker-compose --profile transformer up --build
   ```

### Port Configuration

If port 1313 is already in use, edit `docker-compose.yml`:

```yaml
hugo:
  ports:
    - "8080:1313"  # Change 8080 to any available port
```

Then access at: http://localhost:8080

## Troubleshooting

### Permission Issues (Linux/Mac)

**Problem:** Cannot execute helper scripts

**Solution:**
```bash
chmod +x *.sh
```

**Problem:** Docker permission denied

**Solution:**
```bash
# Add your user to docker group
sudo usermod -aG docker $USER

# Log out and log back in
```

### Port Already in Use

**Error:** `port is already allocated`

**Solution:** Change the port mapping in `docker-compose.yml` as shown above

### Changes Not Appearing

**Problem:** Code changes not reflected in container

**Solution:**
```bash
# Rebuild the container
docker-compose --profile hugo up --build

# Or clear cache completely
docker-compose down
docker-compose --profile hugo build --no-cache
docker-compose --profile hugo up
```

### Data Transformer Fails

**Problem:** Cannot fetch data from API

**Checklist:**
1. Check internet connection
2. Verify API endpoint is accessible:
   ```bash
   curl https://support.knowbe4.com/api/v2/help_center/en-us/articles.json
   ```
3. Check transformer logs:
   ```bash
   docker-compose --profile transformer up
   ```
4. Debug inside container:
   ```bash
   docker-compose --profile transformer run transformer /bin/sh
   # Then run: python data_transformer.py
   ```

### Hugo Build Errors

**Problem:** Hugo build fails

**Solution:**
1. Check Hugo version compatibility
2. Verify `site_src/hugo.toml` syntax
3. Check Hugo logs for specific errors
4. Test Hugo directly:
   ```bash
   docker-compose --profile hugo run hugo version
   ```

## Docker Cleanup

### Remove Containers

```bash
# Stop and remove containers
docker-compose down

# Remove containers and volumes
docker-compose down -v
```

### Remove Images

```bash
# Remove project images
docker-compose down --rmi all

# Remove all unused images
docker image prune -a
```

### Complete Cleanup

```bash
# Remove everything (containers, images, networks, volumes)
docker system prune -a --volumes
```

**Warning:** This removes ALL Docker resources, not just this project!

## Benefits of Docker Approach

✅ **Consistency:** Everyone uses the same Hugo and Python versions
✅ **Simplicity:** No need to install Hugo or Python locally  
✅ **Testing:** Preview changes before pushing to GitHub  
✅ **Isolation:** Won't conflict with other projects  
✅ **Portability:** Works identically on Windows, Mac, and Linux

## FAQ

**Q: Do I have to use Docker?**  
A: No! Docker is completely optional. Your existing workflow still works.

**Q: Will this change my GitHub Actions deployment?**  
A: No. GitHub Actions continues to work exactly as before.

**Q: Can I run both services at once?**  
A: Yes, but typically you don't need to. They're designed to run independently.

**Q: Where are files stored?**  
A: All files are on your local filesystem. Docker containers are ephemeral; data persists through volume mounts.

**Q: How do I remove Docker from this project?**  
A: Delete the `Dockerfile*`, `docker-compose.yml`, `.dockerignore`, helper scripts (`*.sh`, `*.bat`), and `DOCKER.md`. No other changes needed.

**Q: Does this work on Windows?**  
A: Yes! Use the `.bat` scripts instead of `.sh` scripts. Everything else is identical.

**Q: What's the difference between `hugo` and `hugo-build` services?**  
A: 
- `hugo`: Runs development server with live reload (for testing)
- `hugo-build`: Builds static files once (like GitHub Actions)

## Advanced Usage

### Custom Environment Variables

Add environment variables to `docker-compose.yml`:

```yaml
transformer:
  environment:
    - API_KEY=your_key_here
    - BASE_URL=https://custom-api.com
```

Then access in Python:
```python
import os
api_key = os.getenv('API_KEY')
```

### Using Different Output Directories

Edit `docker-compose.yml` volume mounts:

```yaml
transformer:
  volumes:
    - ./custom_output:/app/site_src/static
```

### Running Commands Inside Containers

```bash
# Get a shell inside the transformer container
docker-compose --profile transformer run transformer /bin/sh

# Get a shell inside the Hugo container  
docker-compose --profile hugo run hugo /bin/sh

# Run custom Hugo command
docker-compose --profile hugo run hugo --help
```

## Maintenance

### Updating Docker Images

```bash
# Pull latest base images
docker pull python:3.11-slim
docker pull klakegg/hugo:0.120.4-ext-alpine

# Rebuild your images
docker-compose build
```

### Viewing Logs

```bash
# View transformer logs
docker-compose --profile transformer logs

# View Hugo logs
docker-compose --profile hugo logs

# Follow logs in real-time
docker-compose --profile hugo logs -f
```

## Production Deployment

**Important:** Docker is for local development only. Production deployment uses GitHub Actions and is unchanged.

Production workflow:
1. Develop and test locally with Docker
2. Commit changes to Git
3. Push to GitHub
4. GitHub Actions automatically builds and deploys
5. Changes appear on GitHub Pages

Docker is NOT used in production deployment.

---

## Support

For issues specific to:
- **Docker setup:** See this documentation
- **Data transformer:** Check `data_transformer.py`
- **Hugo configuration:** See `site_src/hugo.toml`
- **GitHub Actions:** See `.github/workflows/hugo.yaml`
- **General project:** See `README.md` and `TECHNICAL_RESEARCH_STUDY.md`

---

**Docker Version:** 1.0  
**Last Updated:** November 2025  
**Tested On:** Docker Desktop 4.25+, Docker Compose 2.0+
