import os
import json
from PIL import Image

image_dir = "data/images"
output_json = "data/annotations.json"

coco = {
    "info": {},
    "licenses": [],
    "images": [],
    "annotations": [],
    "categories": [
    {"id": 1, "name": "background"},
    {"id": 2, "name": "leaf"},
    {"id": 3, "name": "silkworm"}
]

}

image_id = 1
for filename in sorted(os.listdir(image_dir)):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(image_dir, filename)
        try:
            with Image.open(path) as img:
                width, height = img.size
        except:
            continue
        coco["images"].append({
            "id": image_id,
            "file_name": filename,
            "width": width,
            "height": height
        })
        image_id += 1

with open(output_json, "w") as f:
    json.dump(coco, f, indent=2)

print(f"Generated COCO JSON at {output_json} with {len(coco['images'])} images.")
