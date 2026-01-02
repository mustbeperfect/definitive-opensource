import json

"""

# Load the JSON data from file
with open("../../data/dynamic/applications.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert all platform entries to lowercase
for app in data.get("applications", []):
    if "platforms" in app and isinstance(app["platforms"], list):
        app["platforms"] = [platform.lower() for platform in app["platforms"]]

# Write the modified data back to the file
with open("../../data/dynamic/applications.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("All platform entries have been converted to lowercase.")
"""

"""
# Load the JSON file
with open("../../data/dynamic/applications.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Add "flags" and "stars" properties to each application
for app in data.get("applications", []):
    app["homepage_url"] = ""

# Save the updated JSON back to the file
with open("../../data/dynamic/applications.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Operation successful: applications.json updated")
"""

# Load applications.json
with open("../../data/dynamic/applications.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Platforms to check for
move_to_tags = {"cli", "cli-plus", "tui", "pip"}

for app in data.get("applications", []):
    platforms = app.get("platforms", [])
    tags = set(app.get("tags", []))

    # Move matching items to tags
    new_platforms = []
    for p in platforms:
        if p in move_to_tags:
            tags.add(p)
        else:
            new_platforms.append(p)
    
    # Update the application
    app["platforms"] = new_platforms
    app["tags"] = sorted(tags)

# Save the updated file
with open("../../data/dynamic/applications.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
