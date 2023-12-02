import json

with open('resources/day_18.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    d = json.loads(line)
    pass