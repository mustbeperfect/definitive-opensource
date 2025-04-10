
# The Portal
The place that connects everything related to definitive-opensource.

### Lists
- [ALL](README.md)
- [Windows](readmes/windows.md)
- [MacOS](readmes/macos.md)
- [Linux](readmes/linux.md)
- [Selfhost](readmes/selfhost.md)

### Contributing
- [CONTRIBUTING](.github/CONTRIBUTING.md) - Goes over how to contribute, conventions, etc
- [GUIDELINES](.github/GUIDELINES.md) - Guidelines for what qualifies a project to be added

### Development
- [ARCHITECTURE.md](resources/dev/ARCHITECTURE.md) - Explains the "backend" of the list
- [source/scripts/generation](source/scripts/generation) - Contains scripts related to README generation
- [source/scripts/maintenance](source/scripts/maintenance) - Contains scripts related to maintenance

## Data
- [applications.json](source/data/applications.json) - Stores all information related to applications
- [categories.json](source/data/categories.json) - Declares categories and subcategories
- [tags](source/data/tags.json) - Declares tags, their id, and corresponding emoji

## GitHub Actions
- [generate-readme.yml](.github/workflows/generate-readme.yml) - Calls the [```readme_generator.py```](source/scripts/generation/readme_generator.py) to generate READMEs
- [update-stats.yml](.github/workflows/update-stats.yml) - Calls the [```stats_updator.py```](source/scripts/maintenance/stats_updator.py.py) to update stats in applications.json

## Other Resources
- [DOCS.md](resources/DOCS.md) - Elaborates tags
