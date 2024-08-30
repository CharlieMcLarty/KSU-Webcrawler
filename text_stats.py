import json

with open('output.json', encoding='utf8') as f:
    data = json.load(f)

for row in data:
    print(row['url'], 'Email Count', len(row['email']))
