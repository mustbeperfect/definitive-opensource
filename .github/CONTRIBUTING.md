
# Contributing Guidelines

Please note that this project is released with a [Contributor Code of Conduct](CODE-OF-CONDUCT.md). By participating in this project, you agree to abide by its terms.

## Table of Contents
- [A Quick Note](a-quick-note)
- [Conventions](conventions)
- [Guidelines](guidelines)
- [How To Contribute](how-to-contribute)

## A Quick Note
The scale of what this project is attempting to accomplish is one that can only be done collectively. All contributions are highly valued. For submission guidelines on projects, please consult the [submission guidelines](guidelines.md)

>[!IMPORTANT]
>When possible, please edit the file directly and start a pull request instead of raising an issue. DO NOT EDIT THE README. Edit applications.json.

## Conventions
To establish uniformity accross the project, please adhere to these conventions.
- Use the project's official name, not the repository name. Repository names often use lowercase and place dashes in place of spaces. Fallback to **Title Casing** if capitalization is not clear. 
- Platform tags are listed in the following order: ```Desktop OS (Order: Windows, MacOS, Linux)```, ```Mobile (Order: Android, IOS)```, ```CLI```, ```SelfHost```, ```Web```, ```Plugin```
- For projects with multiple repositories (EX: one for IOS, Windows, etc) link the repository with the most stars.
- The description should be the repository description. If there are multiple repositories, no description, or an inadequate one, fall back to the organization, their official website, or the repo's README. **Do not write your own description, only use text from official sources of the project, and do not modify (EX: shorten) their description.** The ONLY change you can make is replacing ```|``` with ```-``` to prevent interference with GFM tables. If you not using the GitHub description, put the ```custom-description``` flag in the flags array so our description updator script does not override it. 
- For tags, do not use the emoji. Go to [tags.json](source/data/tags.json) and find the id for the tag. Our script will generate it's corresponding emoji when it builds the README. 

## Guidelines
- Check the archive, the backlog, and duplicates
- Make sure the category is fitting
- The pull request and commit should have concise and descriptive titles
- One pull request per new addition
- If a project is in the grey zone for submission guidelines, include why it should be included.
- Proposals for new categories or the re-organization of existing categories must be discussed and approved via an issue prior to the pull request

## How To Contribute
[How to create a pull request.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

- Fork the repo
- Edit your changes in the README
- Propose changes

