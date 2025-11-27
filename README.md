# KnowBe4 Static API Replica

This project is a static replica of the KnowBe4 Help Center API (Zendesk V2), built using [Hugo](https://gohugo.io/) and hosted on GitHub Pages. It serves static JSON files that mimic the structure and content of the real API endpoints.

## How It Works

1.  **Data Source**: The core data is stored in JSON files within the `site_src/data/zendesk/` directory:
    *   `categories.json`
    *   `sections.json`
    *   `articles.json`
    These files contain the actual data fetched from the KnowBe4 Help Center.

2.  **Hugo Templating**: Hugo uses layout templates located in `site_src/layouts/api/` to process this data.
    *   Instead of rendering HTML, these templates use Hugo's `jsonify` function to output the data directly as valid JSON.
    *   The templates are mapped to specific URLs using content stubs in `site_src/content/api/v2/help_center/en-us/`.

3.  **Deployment**:
    *   A GitHub Actions workflow (`.github/workflows/hugo.yaml`) triggers on every push to the `main` branch.
    *   It builds the Hugo site and deploys the generated `public/` directory to the `gh-pages` branch.
    *   GitHub Pages serves these static files, making them accessible via public URLs.

## API URLs for Google GEMs

Use the following URLs to access the static API endpoints. These are the URLs you should provide to your Google GEMs or other tools that need to consume this data.

### Base URL
`https://Criscras13.github.io/API_testing/`

### Endpoints

*   **Categories**:
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/categories.json
    ```

*   **Sections**:
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/sections.json
    ```

*   **Articles**:
    ```
    https://Criscras13.github.io/API_testing/api/v2/help_center/en-us/articles.json
    ```

## Updating Data

To update the data served by this API:
1.  Replace the JSON files in `site_src/data/zendesk/` with new data.
2.  Commit and push the changes to the `main` branch.
3.  The site will automatically rebuild and deploy the updated data.
