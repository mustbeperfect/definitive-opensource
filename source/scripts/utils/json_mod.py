import json

# Load the JSON data from file
with open("source/data/applications.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert all platform entries to lowercase
for app in data.get("applications", []):
    if "platforms" in app and isinstance(app["platforms"], list):
        app["platforms"] = [platform.lower() for platform in app["platforms"]]

# Write the modified data back to the file
with open("source/data/applications.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("All platform entries have been converted to lowercase.")


"""
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
"""