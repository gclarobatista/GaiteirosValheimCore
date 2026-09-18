#!/usr/bin/env python3
"""Build the exact Thunderstore upload archive from the reviewed package files."""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).parent
package = root / "package"
manifest = json.loads((package / "manifest.json").read_text())
version = manifest["version_number"]
archive = root / "dist" / f"GateirosValheimCore-{version}.zip"
archive.parent.mkdir(exist_ok=True)

with ZipFile(archive, "w", ZIP_DEFLATED) as output:
    for filename in ("manifest.json", "README.md", "CHANGELOG.md", "icon.png"):
        output.write(package / filename, filename)

print(archive)
