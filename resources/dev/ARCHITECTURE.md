
# Architecture
Here's a look at how the "backend" of the list works. 

## README Generation
All applications are stored inside [`applications.json`](source/data/applications.json). Categories are declared inside [`categories.json`](source/data/categories.json). Instead of a nested format with subcategories as on object of it's parent, we've given subcategories a `parent` attribute. There's also a [`tags.json`](source/data/tags.json). Instead of putting the emoji inside of the ```tags``` attribute in `applications.json`, the id is used, for example, `commercial` or `disruptive`.. These id's are mapped to their corresponding emoji for when the READMEs are generated and makes``applications.json``` more readable. 

The generation scripts are inside of the [`source/scripts/generation`](source/scripts/generation) directory. [`mainheader_generator.py`](source/scripts/generation/mainheader_generator.py) generates the very top header with the dynamic project count. Then, depending on the platform being generating, it inserts [`header.md`](source/components/header.md), [`macosheader.md`](source/components/macosheader.md), etc.

[`tableofcontents_generator.py`](source/scripts/generation/tableofcontents_generator.py) generates the table of contents. It creates one, expandable but hidden by default, with all subsections listed alphabetically. The default TOC shows parent categories alphabetically with subcategories underneath, also alphabetically.

[`contents_generator.py`](source/scripts/generation/contents_generator.py) generates the actual list.

Lastly [`readme_generator.py`](source/scripts/generation/readme_generator.py) brings everything together, calling the other scripts to generate one main list, and more for several platforms. 

## Maintenence
[`applications.json`](source/data/applications.json) stores a lot of information that the README does not display such as last commit, language, and license. These are for a future web version of the list that would pull data from the json file. [`stats_updator.py`](source/maintenance/stats_updator.py) runs every midnight and updates all application stats. Each application object in the json file also has a `flags` attribute. For example, the `custom-description` flag tells the stats_updator script to skip updating the description for that app. For more into on flags, consult the [`DOCS.md`](resources/DOCS.md)