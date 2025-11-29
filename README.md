# KnowBe4 Static API Replica

This project is a static replica of the KnowBe4 Help Center API (Zendesk V2), built using [Hugo](https://gohugo.io/) and hosted on GitHub Pages. It serves static JSON files that mimic the structure and content of the real API endpoints.

## How It Works

1.  **Data Generation**: A Python script (`data_transformer.py`) fetches fresh data from the KnowBe4 API:
    *   Fetches categories, sections, and articles via API calls
    *   Rewrites URLs to point to this GitHub Pages site
    *   Generates both `.json` files (for API clients) and `.html` wrapper files (for AI browsing tools)
    *   Saves all files directly to `site_src/static/api/v2/help_center/en-us/`

2.  **Static Site Building**: Hugo is used as a simple static file copier:
    *   Hugo copies all files from `site_src/static/` to the output directory
    *   No template processing or data transformation occurs in Hugo
    *   The site is pre-built with all JSON and HTML files ready to serve

3.  **Deployment**:
    *   A GitHub Actions workflow (`.github/workflows/hugo.yaml`) triggers on every push to the `main` branch
    *   It builds the Hugo site and deploys the generated `public/` directory to the `gh-pages` branch
    *   GitHub Pages serves these static files, making them accessible via public URLs

## API Endpoints

**Base URL:** `https://Criscras13.github.io/API_testing/`

This API is available in two formats:

### For AI Agents/Browsers (Google GEMs, etc.)

**Use these `.html` URLs if you are using AI tools that browse webpages:**

*   **Categories:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/categories.html
    ```

*   **Sections:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/sections.html
    ```

*   **Articles:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/articles.html
    ```

*   **Individual Articles:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/articles/{id}.html
    ```

These HTML endpoints display the JSON data wrapped in HTML `<pre>` tags, making them accessible to AI browsing tools that require `text/html` content type.

---

### For API Clients (Programmatic Access)

**Use these `.json` URLs if you are writing code or using API clients:**

*   **Categories:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/categories.json
    ```

*   **Sections:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/sections.json
    ```

*   **Articles:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/articles.json
    ```

*   **Individual Articles:**
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/articles/{id}.json
    ```

These JSON endpoints serve raw JSON data with `application/json` content type.


## Updating Data

To update the data served by this API, you have two options:

### Option 1: Using Docker (Recommended)

If you have Docker installed, use the helper scripts:

```bash
# Linux/Mac
./update-data.sh

# Windows
update-data.bat
```

This will fetch fresh data and save it to `site_src/static/`.

### Option 2: Traditional Method

Run the Python script directly:

```bash
python data_transformer.py
```

*Note: This requires Python 3.x and internet access to reach `support.knowbe4.com`.*

### After Running Either Method

1.  **Commit and Push**:
    After the data is updated, commit the updated files and push to the `main` branch.
    ```bash
    git add site_src/static/
    git commit -m "Update API data"
    git push origin main
    ```

2.  **Automatic Deployment**:
    The GitHub Actions workflow will automatically rebuild the site and deploy the updated data to GitHub Pages.

## 🐳 Docker Setup (Optional)

Docker support is available for local development and testing. This makes it easy to work on the project without installing Hugo or Python locally.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed
- Docker Compose (included with Docker Desktop)

### Quick Start with Docker

#### Fetch Fresh API Data
```bash
# Linux/Mac
./update-data.sh

# Windows
update-data.bat
```

#### Run Local Hugo Server
```bash
# Linux/Mac
./serve-local.sh

# Windows
serve-local.bat

# Visit http://localhost:1313 to view your site
```

#### Build Static Site
```bash
# Linux/Mac
./build-site.sh

# Windows
build-site.bat
```

### Why Use Docker?

✅ **Consistent Environment:** Same Hugo version and Python dependencies for everyone  
✅ **No Local Installation:** Don't need to install Hugo or Python on your machine  
✅ **Easy Testing:** Test changes locally before pushing to GitHub  
✅ **Isolation:** Won't conflict with other projects

### Traditional Workflow (Still Works!)

The traditional workflow (running `data_transformer.py` directly and using GitHub Actions for deployment) continues to work unchanged. Docker is purely optional for local development.

**For detailed Docker documentation, see [DOCKER.md](DOCKER.md).**
