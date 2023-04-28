import json

with open('icons.json', 'r') as iconsR:
    icons = json.load(iconsR)

with open('icons.min.json', 'w') as iconsW:
    json.dump(icons, iconsW)