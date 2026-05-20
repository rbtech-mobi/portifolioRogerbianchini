python
import json
from datetime import datetime
# Lê o projects.json atual
with open("data/projects.json", "r") as f:
    projects = json.load(f)
# Atualiza o metadata
meta = {
    "last_updated": datetime.now().strftime("%B %d, %Y"),
    "total_projects": len(projects),
    "active": len([p for p in projects if p.get("status") == "active"])
}
with open("data/meta.json", "w") as f:
    json.dump(meta, f, indent=2)
print(f"Updated: {meta['last_updated']}")
