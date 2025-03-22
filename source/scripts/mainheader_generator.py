import json

def generate_mainheader():
    with open("source/data/applications.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    project_count = len(data.get("applications", []))
    
    header_content = f"""
<table align="center">
    <tr>
    <td>🇺🇦 v0.5.2-beta</td>
    </tr>
</table>

<h1 align="center">[ definitive-opensource ] </h1>
<p align="center">A definitive list of the best of everything open source</p>

<p align="center"><code>Status: Active</code> - <code>Projects: {project_count}</code></p>
"""
    
    return header_content

if __name__ == "__main__":
    generate_mainheader()
