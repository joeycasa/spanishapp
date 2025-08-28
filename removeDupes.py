import json

# Load your JSON file
with open("sentences.json", "r", encoding="utf-8") as f:
    sentences = json.load(f)

# Remove duplicates
seen = set()
unique_sentences = []
for s in sentences:
    key = (s["spanish"], s["english"])  # consider both fields
    if key not in seen:
        seen.add(key)
        unique_sentences.append(s)

# Overwrite the original file
with open("sentences.json", "w", encoding="utf-8") as f:
    json.dump(unique_sentences, f, ensure_ascii=False, indent=2)

print(f"Removed duplicates. {len(sentences) - len(unique_sentences)} duplicates were found.")
