
import json
import os
from pathlib import Path

BASE_DIR = Path("site_src/static/api/v2/help_center/en-us/experimental")
ARTICLES_DIR = BASE_DIR / "articles"
OLD_PATH = "/API_testing/api/v2/"
NEW_PATH = "/API_testing/site_src/static/api/v2/"

def generate_html_wrapper(json_data, title="Data"):
    """Generate HTML wrapper for JSON data."""
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <pre>{json.dumps(json_data, indent=2)}</pre>
</body>
</html>"""

def fix_url(url):
    if OLD_PATH in url and NEW_PATH not in url:
        return url.replace(OLD_PATH, NEW_PATH)
    return url

def process_file(file_path, title_prefix=""):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    
    # Fix top-level URLs
    if 'url' in data:
        data['url'] = fix_url(data['url'])
        modified = True
    if 'html_url' in data:
        data['html_url'] = fix_url(data['html_url'])
        modified = True
        
    # Fix URLs in lists (e.g. articles.json)
    if isinstance(data, list):
        for item in data:
            if 'url' in item:
                item['url'] = fix_url(item['url'])
                modified = True
            if 'html_url' in item:
                item['html_url'] = fix_url(item['html_url'])
                modified = True
                
    # Fix URLs in dicts (e.g. image_index.json)
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                if 'article_url' in value:
                    value['article_url'] = fix_url(value['article_url'])
                    modified = True
                if 'article_html_url' in value:
                    value['article_html_url'] = fix_url(value['article_html_url'])
                    modified = True
                if 'url' in value:
                    # Check if this is an image URL or article URL
                    # Image URLs might be external or relative, but if they match the pattern, fix them
                    value['url'] = fix_url(value['url'])
                    modified = True

    if modified:
        # Save JSON
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        # Save HTML wrapper
        html_path = file_path.with_suffix('.html')
        title = f"{title_prefix} {file_path.stem}"
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(generate_html_wrapper(data, title))
        print(f"  Fixed and saved {file_path} and {html_path}")
    else:
        print(f"  No changes needed for {file_path}")

def main():
    # Fix individual articles
    if ARTICLES_DIR.exists():
        for article_file in ARTICLES_DIR.glob("*.json"):
            process_file(article_file, "Article")
            
    # Fix main indexes
    for filename in ["articles.json", "image_index.json", "topics_to_images.json"]:
        file_path = BASE_DIR / filename
        if file_path.exists():
            process_file(file_path, filename.replace(".json", "").replace("_", " ").title())

if __name__ == "__main__":
    main()
