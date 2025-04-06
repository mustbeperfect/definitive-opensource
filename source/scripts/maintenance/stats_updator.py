import json
import requests
import os
from datetime import datetime

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN') 
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_repo_data(owner, repo):
    repo_url = f'https://api.github.com/repos/{owner}/{repo}'
    commits_url = f'{repo_url}/commits'

    repo_response = requests.get(repo_url, headers=HEADERS)
    commit_response = requests.get(commits_url, headers=HEADERS)

    if repo_response.status_code != 200:
        print(f"Failed to fetch data for {owner}/{repo}")
        return {}

    repo_data = repo_response.json()
    commits_data = commit_response.json()

    last_commit_date = ''
    if isinstance(commits_data, list) and len(commits_data) > 0:
        last_commit_date = commits_data[0]['commit']['committer']['date']
        last_commit_date = datetime.strptime(last_commit_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%m/%d/%Y")

    return {
        'description': repo_data.get('description', ''),
        'stars': repo_data.get('stargazers_count', 0),
        'language': repo_data.get('language', ''),
        'license': repo_data.get('license', {}).get('spdx_id', '') if repo_data.get('license') else '',
        'last_commit': last_commit_date
    }

def update_applications(filepath='source/data/applications.json'):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for app in data.get('applications', []):
        try:
            url = app['link']
            if "github.com" not in url:
                continue
            parts = url.split('/')
            owner, repo = parts[3], parts[4]
            print(f"Updating: {owner}/{repo}")

            updated_info = get_repo_data(owner, repo)

            app['description'] = updated_info.get('description', app['description'])
            app['stars'] = updated_info.get('stars', app['stars'])
            app['language'] = updated_info.get('language', app['language'])
            app['license'] = updated_info.get('license', app['license'])
            app['last_commit'] = updated_info.get('last_commit', app['last_commit'])

        except Exception as e:
            print(f"Error updating {app.get('name')}: {e}")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print("Update complete!")

if __name__ == "__main__":
    update_applications()
