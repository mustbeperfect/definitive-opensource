import os
import requests
import json
from datetime import datetime
import os

with open('../../data/dynamic/applications.json', 'r') as f:
    data = json.load(f)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def update_application_data(app):

    repo_name = app["repo_url"].split("github.com/")[1]
    

    repo_url = f'https://api.github.com/repos/{repo_name}'

    print(f"Updating: {repo_name}")
    print(f"API URL: {repo_url}")


    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()

        app['stars'] = repo_data.get('stargazers_count', app['stars'])
        app['language'] = repo_data.get('language', app['language'])

        if 'custom-homepage' not in app.get('flags', []):
            app['homepage_url'] = repo_data.get('homepage', app['homepage_url'])

        if 'custom-description' not in app.get('flags', []):
            app['description'] = repo_data.get('description', app.get('description'))
        
        if 'custom-license' not in app.get('flags', []):
            license_data = repo_data.get('license')
            if license_data is not None:
                app['license'] = license_data.get('spdx_id', app['license'])
            else:
                app['license'] = app['license']
        
        app['last_commit'] = datetime.strptime(repo_data['pushed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y')

        return app
    else:
        print(f"Error: Unable to fetch data for {repo_name}. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return app

for app in data['applications']:
    app = update_application_data(app)

with open('../../data/dynamic/applications.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated application data successfully!")
