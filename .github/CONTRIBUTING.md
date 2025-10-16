
# Contributing Guidelines
Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## Table of Contents
- [A Quick Note](a-quick-note)
- [Conventions](conventions)
- [Guidelines](guidelines)
- [How To Contribute](how-to-contribute)

## A Quick Note
The scale of what this project is attempting to accomplish is one that can only be done collectively. All contributions are highly valued. For submission guidelines on projects, please consult the [submission guidelines](GUIDELINES.md)

>[!IMPORTANT]
>When possible, please edit the file directly and start a pull request instead of raising an issue. DO NOT EDIT THE README. Edit applications.json.

## Conventions
To establish uniformity accross the project, please adhere to these conventions.
- Use the project's official name, not the repository name. Repository names often use lowercase and place dashes in place of spaces. Fallback to **Title Casing** if capitalization is not clear. 
- For projects with multiple repositories (EX: one for IOS, Windows, etc) link the repository with the most stars.
- Do not put in a description unless the repo description is inadequate or non-existent, in which case fall back to the organization, their website, or the repo's README. **Do not write your own description, only use text from official sources of the project, and do not modify (EX: shorten) their description.** If you use a custom description make sure to put in the `custom-description` flag so that the stat updator script doesn't overide it. 
- For tags, do not use the emoji. Go to [tags.json](source/data/static/tags.json) and find the id for the tag. Our script will generate it's corresponding emoji when it builds the README. 

## How To Contribute
[How to create a pull request.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

Open applications.json and copy the following at the end:
```json
{
    "name": "",
    "description": "",
    "repo_url": "",
    "tags": [],
    "platforms": [
        ""
    ],
    "category": "",
    "stars": 0,
    "flags": [],
    "last_commit": "",
    "language": "",
    "license": "",
    "homepage_url": ""
}
```

Add the `name`, `repo_url`, `tags`, `platform(s)`, and `category`. Everything else will be filled in once the daily stats_updator script runs. 

## Guidelines
- Check the archive, the backlog, and duplicates
- Make sure the category is fitting
- The pull request and commit should have concise and descriptive titles
- One pull request per new addition
- If a project is in the grey zone for submission guidelines, include why it should be included.
- Proposals for new categories or the re-organization of existing categories must be discussed and approved via an issue prior to the pull request
