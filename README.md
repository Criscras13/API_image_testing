# API Image Testing Repository

> **Experimental Repository** - AI-Enhanced Knowledge Base with Visual Search

---

## 🚀 Overview

This repository demonstrates advanced AI-powered documentation indexing using **Gemini Flash 2.0** for visual content analysis. Every screenshot in the KnowBe4 Help Center has been enriched with detailed AI-generated descriptions, enabling semantic visual search.

### Key Features

*   **3,519 AI-Described Images** - Every screenshot analyzed by Gemini Flash with detailed descriptions of UI elements, buttons, and workflows
*   **640 Searchable Topics** - Semantic topic index mapping keywords to relevant images
*   **1,004 Enhanced Articles** - Complete article metadata with embedded image context
*   **Zero-Cost Deployment** - Static API hosted on GitHub Pages

---

## 🔗 Live API Endpoints

Access the enriched data via GitHub Pages:

### **Visual Search Index**
Find images by topic keyword.
*   **URL:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/topics_to_images.html`
*   **Format:** HTML (AI-optimized) or JSON
*   **Usage:** Search for a keyword (e.g., "webhooks") to get Image IDs

### **Image Metadata Index**
Look up full details for specific Image IDs.
*   **URL:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/image_index.html`
*   **Format:** HTML (AI-optimized) or JSON
*   **Contains:** AI descriptions, article context, image URLs

### **Enhanced Articles List**
Browse all enriched articles.
*   **URL:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles.html`
*   **Format:** HTML list with direct links

### **Enhanced Article Detail**
Access individual article data.
*   **URL Pattern:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles/{article_id}.html`
*   **Example:** [Smart Groups Quickstart](https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles/115015198248.html)

---

## 📊 Data Structure

### Enhanced Article Example
```json
{
  "id": 115015198248,
  "title": "Smart Groups Quickstart Guide",
  "body": "...",
  "images": [
    {
      "url": "https://helpimg.s3.us-east-1.amazonaws.com/...",
      "alt": "Screenshot of the Smart Group Criteria Modal showing...",
      "description": "Detailed AI-generated description of UI elements...",
      "position": 1,
      "context": "Surrounding text from article..."
    }
  ],
  "metadata": {
    "category": "Security Awareness Training",
    "section": "Smart Groups",
    "topics": ["smart", "groups", "criteria", "modal"],
    "image_count": 27
  }
}
```

---

## 🤖 AI Agent Integration

### Gemini (GEM) Configuration

Use these URLs as "Authorized Knowledge Sources":

1.  **Articles List:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/articles.html`
2.  **Visual Search Index:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/topics_to_images.html`
3.  **Image Metadata:** `https://Criscras13.github.io/API_image_testing/site_src/static/api/v2/help_center/en-us/experimental/image_index.html`

**Important:** Configure agents to search for **single keywords** (e.g., "smart" OR "group") rather than phrases when using the Topic Index.

### Sample Agent Workflows

**General Support Questions:**
1. Use `browse` tool on Articles List
2. Find relevant article by title keywords
3. Access article to get content + embedded image metadata
4. Provide answer with clickable image links

**Visual Search Questions:**
1. Use `browse` tool on Visual Search Index
2. Search for single keywords matching user query
3. Extract Image IDs from matches
4. Look up image details in article or Image Metadata

---

## 📖 Technical Documentation

For implementation details, architecture, and AI enrichment pipeline:
*   **[Technical Research Study](TECHNICAL_RESEARCH_STUDY.md)** - Complete technical overview

---

## 🛠 Local Development

### Generate Indexes
```bash
python build_experimental_indexes.py
```

### Update Help Center Data
```bash
.\update-data.bat  # Windows
./update-data.sh   # Linux/Mac
```

---

## 📈 Current Statistics

*   **Images Indexed:** 3,519
*   **Articles Enhanced:** 1,004
*   **Searchable Topics:** 640
*   **Total Index Size:** ~40 MB (optimized)

---

## 🔄 Related Repositories

*   **Production Source:** [API_testing](https://github.com/Criscras13/API_testing) (main branch)
*   **Development Branch:** [phase8-testing-clean](https://github.com/Criscras13/API_testing/tree/phase8-testing-clean)

---

## 📝 License

This is an experimental testing repository. Content is derived from KnowBe4 Help Center documentation.
