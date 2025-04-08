import json

# Load the JSON file
with open("source/data/applications.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Add "flags" and "stars" properties to each application
for app in data.get("applications", []):
    app["homepage_url"] = ""

# Save the updated JSON back to the file
with open("source/data/applications.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Operation successful: applications.json updated")
