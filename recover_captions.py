import json
from pathlib import Path

# Paths
BASE_DIR = Path("site_src/static/api/v2/help_center/en-us")
EXPERIMENTAL_DIR = BASE_DIR / "experimental"
IMAGE_INDEX_FILE = EXPERIMENTAL_DIR / "image_index.json"
OUTPUT_FILE = Path("image_captions.json")

def main():
    print(f"Recovering captions from {IMAGE_INDEX_FILE}...")
    
    if not IMAGE_INDEX_FILE.exists():
        print(f"ERROR: {IMAGE_INDEX_FILE} not found!")
        return

    with open(IMAGE_INDEX_FILE, 'r', encoding='utf-8') as f:
        image_index = json.load(f)
    
    captions = {}
    count = 0
    
    for key, data in image_index.items():
        url = data.get('url')
        description = data.get('description')
        
        if url and description:
            captions[url] = description
            count += 1
            
    print(f"Found {count} captions.")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(captions, f, indent=2)
        
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
