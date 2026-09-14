# Contributing Guidelines
Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## Table of Contents
- [A Quick Note](#a-quick-note)
- [Our AI Policy](#our-ai-policy)
- [Conventions](#conventions)
- [Guidelines](#guidelines)
- [How To Contribute](#how-to-contribute)
- [Submission Guidelines](#submission-guidelines)

## A Quick Note
The scale of what this project is attempting to accomplish is one that can only be done collectively. All contributions are highly valued. 

>[!IMPORTANT]
>When possible, please edit the file directly and start a pull request instead of raising an issue. DO NOT EDIT THE README. Edit applications.json.

## Our AI Policy
I'm not necessarily against AI. I don't like the mass plagiarism LLM's were built on and their regurgative nature, but regardless, it's clear AI isn't going anywhere. I mean I use AI all the time... as a tool. And that's the key. LLM's are incredible, but there are limitations and it's important we don't forget that. 

If your project uses AI as a tool, cool. I don't really care if AI is writing code as long as it's being supervised and is being integrated in a way where it isn't slop.

If your project is vibe-coded, it will not be allowed on this list. How will I know? AI created interfaces are rather easy to spot. The use of AGENTS.md and Claude in your contributor list are also a telling signs.

This is my stance right now. It will likely change as the technology cements itself in the world. 

## Conventions
To establish uniformity accross the project, please adhere to these conventions.
- Use the project's official name, not the repository name. Repository names often use lowercase and place dashes in place of spaces. Fallback to **Title Casing** if capitalization is not clear. 
- For projects with multiple repositories (EX: one for IOS, Windows, etc) link the repository with the most stars.
- Do not put in a description unless the repo description is inadequate or non-existent, in which case fall back to the organization, their website, or the repo's README. **Do not write your own description, only use text from official sources of the project, and do not modify (EX: shorten) their description.** If you use a custom description make sure to put in the `custom-description` flag so that the stat updator script doesn't overide it. 
- For tags, do not use the emoji. Go to [tags.json](/core/data/static/tags.json) and find the id for the tag. Our script will generate it's corresponding emoji when it builds the README. 

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
    "flags": [],
    "license": "",
}
```

Add the `name`, `repo_url`, `tags`, `platform(s)`, and `category`. Everything else will be filled in once the daily stats_updator script runs. 

## Guidelines
- Check the archive, the backlog, and duplicates
- Make sure the category is fitting
- The pull request and commit should be simple. EX: Added `Name` to `category`
- One pull request per new addition
- If a project is in the grey zone for submission guidelines, include why it should be included.
- Proposals for new categories, re-organization of existing categories, or changes to the underlying list system (ex: generation code) must be discussed and approved via an issue prior to a pull request

# Submission Guidelines

This list is for projects that are _directly used_, not projects with the sole purpose of building another project. Development technologies like frameworks or databases are not allowed. _Enterprise systems_ like CRM or marketing are currently not allowed but may be considered once the core of the list is ironed out. 

```Definitive-opensource``` has a **rigorous** vetting process that involves comprehensive research into a project. 

We continously monitor projects on the list and will immediately remove projects that no longer fit the criteria. 

## Criteria
To avoid the clutter trap that many other lists succumb to as they scale, only the best software is included. But "best" is relative. It's mostly guaged based on the following criteria - keep in mind that there can be exceptions. 

Requirements with no exception:
- Must have 1k stars. The most fundamental requirement with no exceptions.
- Must have had a commit in the last year

## What is Open Source?
The project should abide by the [Open Source Definition (OSD)](https://opensource.org/osd). 
The project's license should be an [OSI Approved License](https://opensource.org/licenses). If not, it should fall under the OSD. 

## Projects Not Hosted on GitHub
Most major projects hosted elsewhere have GitHub mirrors. Blender's mirror has 14.7k stars, Krita's has 8k, Gimp has 5.3, etc. The star counts of those mirrors are used. In the rare case that the project does not have a GitHub mirror, other measures will be taken to analyze product popularity.
