import os
import requests
import json
from datetime import datetime

# Load the applications data from the JSON file
with open('source/data/applications.json', 'r') as f:
    data = json.load(f)

# GitHub API token from the environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Headers for the API request
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to get the latest data for each application
def update_application_data(app):
    # Extract repository name from the GitHub URL
    repo_name = app["link"].split("github.com/")[1]
    
    # API URL for the repository
    repo_url = f'https://api.github.com/repos/{repo_name}'

    print(f"Updating: {repo_name}")  # Debugging output to see which repo is being processed
    print(f"API URL: {repo_url}")  # Debugging output to check URL

    # Make the request to the GitHub API
    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        repo_data = response.json()

        # Update the app's fields with the data from the GitHub API
        app['stars'] = repo_data.get('stargazers_count', app['stars'])
        app['language'] = repo_data.get('language', app['language'])
        
        # Update license with SPDX identifier instead of the license name
        app['license'] = repo_data.get('license', {}).get('spdx_id', app['license'])
        
        # Update last commit date
        app['last_commit'] = datetime.strptime(repo_data['pushed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%m/%d/%Y')

        return app
    else:
        print(f"Error: Unable to fetch data for {repo_name}. Status Code: {response.status_code}")  # Print status code
        print(f"Response: {response.text}")  # Print response content for more insight
        return app

# Update the applications data
for app in data['applications']:
    app = update_application_data(app)

# Write the updated data back to the JSON file
with open('source/data/applications.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Updated application data successfully!")
