import json


with open('data.json', 'r') as f:
    saved_weights = json.load(f)
for key in saved_weights:
    print(f"{key} : {len(saved_weights[key])}")