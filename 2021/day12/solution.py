from collections import defaultdict, Counter

with open('input.txt') as f:
    lines = f.read().splitlines()

sections = defaultdict(set)

for line in lines:
    start, end = line.split('-')
    sections[start].add(end)
    if start != 'start':
        sections[end].add(start)

all_paths = []


def find_paths(sections, prev_path, this_cave, cave_dupes=False):
    this_path = prev_path + [this_cave]

    # We've reached the end!
    if this_cave == 'end':
        all_paths.append(this_path)
        return
    # Previously visited small cave
    if this_cave in prev_path and this_cave.lower() == this_cave:
        if cave_dupes:
            return
        elif this_cave == 'start':
            return
        else:
            cave_dupes = True
            for next_cave in sections[this_cave]:
                find_paths(sections, this_path, next_cave, cave_dupes)
    else:
        for next_cave in sections[this_cave]:
            find_paths(sections, this_path, next_cave, cave_dupes)

find_paths(sections, [], 'start')

print(len(all_paths))