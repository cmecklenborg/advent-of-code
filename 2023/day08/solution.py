import re
from collections import defaultdict
from math import lcm


def part_1(file) -> int:
    with open(file) as input:
        lines = input.read().splitlines()

    dirs = [int(d == "R") for d in lines[0]]
    map = defaultdict(tuple)

    for line in lines[2:]:
        key, val = line.split(" = ")
        left, right = re.findall(r"[A-Z]+", val)
        map[key] = (left, right)

    node = "AAA"
    steps = 0

    while node != "ZZZ":
        for d in dirs:
            node = map[node][d]
            steps += 1

    return steps


def part_2(file) -> int:
    with open(file) as input:
        lines = input.read().splitlines()

    dirs = [int(d == "R") for d in lines[0]]
    map = defaultdict(tuple)

    for line in lines[2:]:
        key, val = line.split(" = ")
        left, right = re.findall(r"[\dA-Z]+", val)
        map[key] = (left, right)

    nodes = [x for x in map.keys() if x[-1] == "A"]
    all_steps = []
    for start_node in nodes:
        steps = 0
        node = start_node
        while node[-1] != "Z":
            for d in dirs:
                node = map[node][d]
                steps += 1

        all_steps.append(steps)

    return lcm(*all_steps)


# s1p1 = part_1('sample1.txt')
# print(f'Sample 1, Part 1: {s1p1}')
# assert s1p1 == 2

# s1p2 = part_1('sample2.txt')
# print(f'Sample 2, Part 1: {s1p2}')
# assert s1p2 == 6

# s3p3 = part_2('sample3.txt')
# print(f'Sample 3, Part 2: {s3p3}')
# assert s3p3 == 6

a1 = part_1("input.txt")
print(f"Part 1: {a1}")

a2 = part_2("input.txt")
print(f"Part 2: {a2}")
