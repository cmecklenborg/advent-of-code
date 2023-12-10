from collections import defaultdict


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
    visited = set()
    xmax = len(lines[0])
    ymax = len(lines)
    for xidx in range(xmax):
        for yidx in range(ymax):
            coords = (xidx, yidx)
            if coords not in visited and coords not in loop_map:
                queue = [coords]
                group = set()
                group_closed = True

                while queue:
                    node = queue.pop(0)
                    nx, ny = node[0], node[1]
                    visited.add(node)
                    group.add(node)
                    north_edge = any([(nx, y) in loop_map for y in range(0, ny)])
                    south_edge = any([(nx, y) in loop_map for y in range(ny + 1, ymax)])
                    west_edge = any([(x, ny) in loop_map for x in range(0, nx)])
                    east_edge = any([(x, ny) in loop_map for x in range(nx + 1, xmax)])
                    group_closed = group_closed and north_edge and south_edge and west_edge and east_edge

                    for next in [(nx+1, ny), (nx-1, ny), (nx, ny+1), (nx, ny-1)]:
                        if next[0] < 0 or next[0] >= xmax:
                            continue
                        if next[1] < 0 or next[1] >= ymax:
                            continue
                        if next not in visited and next not in loop_map:
                            queue.append(next)

                print(f'Group: {sorted(group)}')
                print(f'Group of size {len(group)} is closed: {group_closed}')
                if group_closed:
                    inner += len(group)

    return max(loop_map.values()), inner


max_dist, inner_count = pipe_calcs('sample2.txt')
print(f'Part 1: {max_dist}')
print(f'Part 2: {inner_count}')
