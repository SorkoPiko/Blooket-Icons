import json

with open('iconsNew.json', 'r', encoding='utf-8') as iconsR:
    icons = json.load(iconsR)

with open('iconsNew.min.json', 'w') as iconsW:
    json.dump(icons, iconsW)