from collections import defaultdict
from functools import cache


file = 'input.txt'
with open(file) as input:
    lines = input.read().splitlines()


mirrors = defaultdict(str)

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        mirrors[(x, y)] = c

# List of dx, dy tuples
# OG travel direction -> new travel direction
N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
bounce = {
    '|': {N: [N], S: [S], E: [N, S], W: [N, S]},
    '-': {N: [E, W], S: [E, W], E: [E], W: [W]},
    '\\': {N: [W], S: [E], E: [S], W: [N]},
    '/': {N: [E], S: [W], E: [N], W: [S]},
    '.': {N: [N], S: [S], E: [E], W: [W]},
}

max_x = len(lines[0])
max_y = len(lines)


@cache
def next_nodes(node: tuple) -> tuple():
    coords = node[0:2]
    dir = node[2:]
    mirror = mirrors[coords]
    nodes = []
    for next in bounce[mirror][dir]:
        next_coords = (coords[0] + next[0], coords[1] + next[1])
        if next_coords[0] >= 0 and next_coords[0] < max_x and next_coords[1] >= 0 and next_coords[1] < max_y:
            new_node = (*next_coords, *next)
            nodes.append(new_node)

    return tuple(nodes)


def laser_maze(mirrors, start_node) -> int:
    energized = set()
    loop_detector = []
    queue = [start_node]

    while queue:
        this_node = queue.pop(0)
        loop_detector.append(this_node)
        energized.add(this_node[0:2])
        for node in next_nodes(this_node):
            if node not in loop_detector:
                queue.append(node)

    return len(energized)


def all_lasers(mirrors):
    energy = []
    for x in range(0, max_x):
        energy.append(laser_maze(mirrors, (x, 0, *S)))
        energy.append(laser_maze(mirrors, (x, max_y-1, *N)))

    for y in range(0, max_y):
        energy.append(laser_maze(mirrors, (0, y, *E)))
        energy.append(laser_maze(mirrors, (max_x-1, y, *W)))

    print(max(energy))


print(laser_maze(mirrors, start_node=(0, 0, *E)))
all_lasers(mirrors)
