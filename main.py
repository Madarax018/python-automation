from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: python main.py FOLDER")

folder = Path(sys.argv[1]).expanduser().resolve()
if not folder.is_dir():
    raise SystemExit("Folder not found")

for item in list(folder.iterdir()):
    if not item.is_file():
        continue
    category = item.suffix.lower().lstrip(".") or "other"
    destination = folder / category
    destination.mkdir(exist_ok=True)
    target = destination / item.name
    if target.exists():
        print("Skipped:", item.name)
        continue
    item.rename(target)
    print("Moved:", item.name)
