# API Image Testing Repository

> **Note:** This is a dedicated testing repository for AI-Enhanced Knowledge Base features. It hosts a static API with advanced image indexing and visual search capabilities.

---

## 🚀 Overview

This repository hosts a **visually enriched** version of the Help Center documentation. Unlike standard text-only APIs, this dataset includes:

*   **AI-Generated Image Descriptions:** Every screenshot in the documentation has been analyzed by Google's Gemini Flash model to generate detailed textual descriptions of UI elements, buttons, and layouts.
*   **Visual Search Index:** A reverse index that maps semantic topics (e.g., "Webhooks", "Dashboard", "Phishing") to specific images, allowing AI agents to "search" for visual content.
*   **Enhanced Article Metadata:** Articles are served as structured JSON objects containing both the standard body text and a rich `images` array with context and captions.

## 🔗 API Endpoints

This repository serves a static API via GitHub Pages. You can access the data using the following endpoints:

### **1. Visual Search Index**
Use this to find images related to a specific topic.
*   **URL:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/topics_to_images.html`
*   **Format:** HTML (optimized for AI browsing) or JSON.
*   **Usage:** Search the page for a keyword (e.g., "console") to get a list of relevant Image IDs.

### **2. Master Image Metadata**
Use this to look up details for a specific Image ID.
*   **URL:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/image_index.html`
*   **Format:** HTML (optimized for AI browsing) or JSON.
*   **Usage:** Find an Image ID (e.g., `115015198248_1`) to see its full AI description, the article it belongs to, and the surrounding text context.

### **3. Enhanced Articles List**
Use this to browse all available articles in the enhanced format.
*   **URL:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles.html`
*   **Format:** HTML list of links.

### **4. Enhanced Article Detail**
Access the full data for a specific article.
*   **URL Pattern:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles/{article_id}.html`
*   **Example:** [Article 115015198248 (Smart Groups)](https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles/115015198248.html)

---

## 🛠 Data Structure

### **Enhanced Article Object**
```json
{
  "id": 115015198248,
  "title": "Smart Groups Quickstart Guide",
  "body": "...",
  "images": [
    {
      "url": "https://helpimg.s3.us-east-1.amazonaws.com/...",
      "alt": "Screenshot of the Smart Group Criteria Modal showing...",
      "description": "A modal window titled 'Smart Group Criteria'. It contains dropdowns for...",
      "position": 1
    }
  ],
  "metadata": {
    "topics": ["smart", "groups", "criteria", "modal"]
  }
}
```

---

## 📖 Documentation

For a deep dive into the architecture, design decisions, and how the AI enrichment pipeline works, please read the **[Technical Research Study](TECHNICAL_RESEARCH_STUDY.md)** included in this repository.

## 🤖 Agent Instructions

To use this repository with an AI agent (like a GEM), configure it with the following knowledge sources:

1.  **Visual Search Index:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/topics_to_images.html`
2.  **Image Metadata:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/image_index.html`
3.  **Articles List:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles.html`

*Note: Ensure your agent uses a "Single Keyword" search strategy when querying the Topic Index.*
