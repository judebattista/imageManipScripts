import os
from pathlib import Path

# SET source TO YOUR TARGET DIRECTORY
source = "."

extensions = ['jpg', 'jpeg', 'gif', 'png']
files = []
for (dirpath, dirnames, filenames) in os.walk(source):
    files.extend(filenames)
    break

for foo in files:
    p = Path(source + '/' + foo)
    baseName = p.stem
    ext = p.suffix
    if len(ext) == 0:
        p.rename(Path(p.parent, baseName + '.jpg'))
    print(p)

