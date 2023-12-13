import re
from collections import defaultdict
from math import comb


file = 'sample.txt'
with open(file) as input:
    lines = input.read().splitlines()

for line in lines:
    num_arrangements = 1
    groups = [int(g) for g in re.findall(r'\d+', line)]

    op = '[\.?]'
    br = '[#?]'

    regex = f'{op}+?'.join([f'({br}{{{g},}})' for g in groups])
    matches = re.search(regex, line)
    print(f'Line: {line}')
    print(f'Regex: {regex}')
    print(f'Matches: {matches.groups()}')

    for g, m in zip(groups, matches.groups()):
        num_arrangements *= len(m) - g + 1

    print(num_arrangements)
