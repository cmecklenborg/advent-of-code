import json

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    d = json.loads(line)
    pass