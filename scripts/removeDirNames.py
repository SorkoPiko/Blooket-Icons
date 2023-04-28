# Doesn't work lol

import json

with open('withDirNames/icons.json') as iconsRead:
    icons = json.load(iconsRead)

iconsNew = {}

for k, v in icons.items():
    if isinstance(v, dict):
        iconsNew.update(v)
    else:
        iconsNew.update({k: v})

with open('icons.json', 'w') as iconsWrite:
    json.dump(iconsNew, iconsWrite, indent=4)