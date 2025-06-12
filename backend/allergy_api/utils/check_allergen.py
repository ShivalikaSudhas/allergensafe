import json
import os

# Load allergen data
def load_allergens():
    file_path = os.path.join(os.path.dirname(__file__), "../model/allergen_data.json")
    with open(file_path, "r") as f:
        return json.load(f)

allergen_data = load_allergens()

def check_for_allergens(text):
    found_allergens = []
    text_lower = text.lower()

    for allergen in allergen_data:
        for tag in allergen["tags"]:
            if tag.lower() in text_lower:
                found_allergens.append({
                    "allergen": allergen["name"],
                    "tag": tag,
                    "category": allergen["category"],
                    "major": allergen["major"]
                })
    return found_allergens
