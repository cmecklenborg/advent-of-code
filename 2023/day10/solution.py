from collections import defaultdict
import re


# List of dx, dy tuples
parts = {
    '|': [(0, -1), (0, 1)], # N & S
    '-': [(1, 0), (-1, 0)], # E & W
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)]
}


def pipe_calcs(file) -> (int, int):
    with open(file) as input:
        lines = input.read().splitlines()

    pipe_map = defaultdict(tuple)
    loop_map = defaultdict(tuple)
    for yidx, line in enumerate(lines):
        for xidx, tile in enumerate(line):
            if tile in parts.keys():
                pipe_map[(xidx, yidx)] = [(xidx + dx, yidx + dy) for dx, dy in parts[tile]]
            elif tile == 'S':
                start = (xidx, yidx)

    pipe_map[start] = [k for k in pipe_map if start in pipe_map[k]]
    loop_map[start] = 0
    queue = [start]

    while queue:
        node = queue.pop(0)
        for next in pipe_map[node]:
            if next not in loop_map:
                left, right = pipe_map[next][0], pipe_map[next][1]
                loop_map[next] = min(loop_map.get(left, 100000), loop_map.get(right, 100000)) + 1
                queue.append(next)

    inner = 0
    xmax = len(lines[0])
    ymax = len(lines)

    # Valid walls: |, L-*?7, F-*?J
    # Invalid walls: LJ, F7

    for yidx in range(1, ymax):
        for xidx in range(1, xmax):
            coords = (xidx, yidx)
            if coords not in loop_map:
                left_walls = re.findall(r'(\||L-*?7|F-*?J)', lines[yidx][0:xidx])
                right_walls = re.findall(r'(\||L-*?7|F-*?J)', lines[yidx][xidx+1:xmax])
                if left_walls and right_walls:
                    if len(left_walls) % 2 == 1 and len(right_walls) % 2 == 1:
                        inner += 1

    return max(loop_map.values()), inner


max_dist, inner_count = pipe_calcs('input.txt')
print(f'Part 1: {max_dist}')
print(f'Part 2: {inner_count}')
