
# The Portal
The place that connects everything related to definitive-opensource.

### Lists
- [ALL](/README.md)
- [Windows](/readmes/windows.md)
- [MacOS](/readmes/macos.md)
- [Linux](/readmes/linux.md)
- [Selfhost](/readmes/selfhost.md)

### Contributing
- [CONTRIBUTING](/.github/CONTRIBUTING.md) - Goes over how to contribute, conventions, etc
- [GUIDELINES](/.github/GUIDELINES.md) - Guidelines for what qualifies a project to be added

### Development
- [ARCHITECTURE.md](/resources/dev/ARCHITECTURE.md) - Explains the "backend" of the list
- [core/source/generation](/core/source/generation) - Contains scripts related to README generation
- [core/source/maintenance](/core/source/maintenance) - Contains scripts related to maintenance

## Data
- [applications.json](/core/data/dynamic/applications.json) - Stores all information related to applications
- [categories.json](/core/data/static/categories.json) - Declares categories and subcategories
- [tags](/core/data/static/tags.json) - Declares tags, their id, and corresponding emoji

## GitHub Actions
- [generate-readme.yml](/.github/workflows/generate-readme.yml) - Calls the [`readme_generator.py`](/core/source/generation/readme_generator.py) to generate READMEs
- [update-stats.yml](/.github/workflows/update-stats.yml) - Calls the [`stats_updator.py`](/core/source/maintenance/stats_updator.py.py) to update stats in applications.json

## Other Resources
- [DOCS.md](/resources/DOCS.md) - Elaborates tags
