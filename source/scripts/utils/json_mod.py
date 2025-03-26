import json

# Load the JSON file
with open("source/data/applications.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Add "flags" and "stars" properties to each application
for app in data.get("applications", []):
    app["stars"] = ""
    app["flags"] = ""

# Save the updated JSON back to the file
with open("source/data/applications.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Updated applications.json successfully!")
