import json


def update_applications_file(filepath=".../.../data/static/applications.json"):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if "applications" in data:
        for app in data["applications"]:
            app.pop("last_commit", None)
            app.pop("stars", None)

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Successfully updated {filepath}.")


if __name__ == "__main__":
    update_applications_file()