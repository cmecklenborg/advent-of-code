import re
from collections import defaultdict

file = 'input.txt'
with open(file) as input:
    lines = input.read().splitlines()

gal_map = defaultdict(tuple)
gal_count = 1
rows = set(range(0, len(lines)))
cols = set(range(0, len(lines[0])))

for y, line in enumerate(lines):
    galaxies = re.finditer(r'#', line)
    for galaxy in galaxies:
        x = galaxy.start()
        if y in rows: rows.remove(y)
        if x in cols: cols.remove(x)
        gal_map[gal_count] = (galaxy.start(), y)
        gal_count += 1

dist_map = defaultdict(int)

for start_gal in range(1, gal_count):
    for end_gal in range(start_gal + 1, gal_count):
        x1, x2 = gal_map[start_gal][0], gal_map[end_gal][0]
        y1, y2 = gal_map[start_gal][1], gal_map[end_gal][1]
        dx = abs(x1 - x2) + len([x for x in range(min(x1, x2), max(x1, x2)) if x in cols])
        dy = abs(y1 - y2) + len([y for y in range(min(y1, y2), max(y1, y2)) if y in rows])
        dist_map[(start_gal, end_gal)] = abs(dx) + abs(dy)

print(len(dist_map))
print(sum(dist_map.values()))
