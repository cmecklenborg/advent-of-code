import re

file = 'sample.txt'
with open(file) as input:
    lines = input.read().splitlines()


def find_matches(springs, groups):
    matches = []
    if not groups:
        return 1 if not springs else 0
    group = groups.pop(0)
    max_idx = sum(groups) + len(groups)
    for idx in range(0, len(springs) - max_idx):
        this_spring = springs[idx:idx+group]
        next_spring = springs[idx+group:]
        if all([c in '#?' for c in this_spring]):
            print(f'Found match {this_spring} for group size {group}')
            find_matches(next_spring, groups)

    return sum(matches)


for line in lines:
    num_arrangements = 0
    groups = [int(x) for x in re.findall(r'\d+', line)]
    springs = line.split(' ')[0]

    print(f'Springs: {springs} with groups {groups}')
    print(find_matches(springs, groups))
