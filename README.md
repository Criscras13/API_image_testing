# Static API Replica

This project is a static replica of the a Help Center API (V2), built using [Hugo](https://gohugo.io/) and hosted on GitHub Pages. It serves static JSON files that mimic the structure and content of the real API endpoints.

## How It Works

1.  **Data Source**: The core data is stored in JSON files within the `site_src/data/` directory:
    *   `categories.json`
    *   `sections.json`
    *   `articles.json`
    These files contain the actual data fetched from the Help Center.

2.  **Hugo Templating**: Hugo uses layout templates located in `site_src/layouts/api/` to process this data.
    *   Instead of rendering HTML, these templates use Hugo's `jsonify` function to output the data directly as valid JSON.
    *   The templates are mapped to specific URLs using content stubs in `site_src/content/api/v2/help_center/en-us/`.

3.  **Deployment**:
    *   A GitHub Actions workflow (`.github/workflows/hugo.yaml`) triggers on every push to the `main` branch.
    *   It builds the Hugo site and deploys the generated `public/` directory to the `gh-pages` branch.
    *   GitHub Pages serves these static files, making them accessible via public URLs.

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

To update the data served by this API:

1.  **Run the Data Transformer**:
    This project includes a Python script `data_transformer.py` that fetches fresh data from the API, rewrites the URLs to point to this GitHub Pages site, and saves both JSON files (for API clients) and HTML wrapper files (for AI browsing tools).
    ```bash
    python data_transformer.py
    ```
    *Note: This script requires internet access to reach `the supporting site`.*

2.  **Commit and Push**:
    After the script completes, commit the updated files in `site_src/data/` and `site_src/static/` and push to the `main` branch.
    ```bash
    git add site_src/data/ site_src/static/
    git commit -m "Update API data"
    git push origin main
    ```

3.  **Automatic Deployment**:
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
