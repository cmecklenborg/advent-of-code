import re
from itertools import product
import time

file = 'sample2.txt'
with open(file) as input:
    lines = input.read().splitlines()

num_arrangements = 0
pot_arrangements = 0
start = time.time()

for line in lines:
    springs, buckets = line.split(' ')
    groups = [int(g) for g in re.findall(r'\d+', buckets)]
    num_groups = len(groups)

    op = '[.?]'
    br = '[#?]'

    lazy = f'^{op}*?' + f'{op}+?'.join([f'({br}{{{g}}})' for g in groups]) + f'{op}*?$'
    greedy = f'^{op}*' + f'{op}+'.join([f'({br}{{{g}}})' for g in groups]) + f'{op}*$'

    lazy_matches = re.search(fr'{lazy}', springs)
    greedy_matches = re.search(greedy, springs)
    lazy_starts = [lazy_matches.start(x) for x in range(1, len(lazy_matches.groups()) + 1)]
    greedy_starts = [greedy_matches.start(x) for x in range(1, len(greedy_matches.groups()) + 1)]


    arrangements = product(*[list(x for x in range(lazy_starts[g], greedy_starts[g] + 1) if '.' not in springs[x:x+groups[g]]) for g in range(0, num_groups)])

    for arr in arrangements:
        valid_overlaps = all([arr[idx] > arr[idx-1] + groups[idx-1] for idx in range(1, len(arr))])
        between_chars = ''.join([springs[arr[idx-1] + groups[idx-1]:arr[idx]] for idx in range(1, len(arr))])

        if valid_overlaps and not '#' in between_chars:
            num_arrangements += 1

print(num_arrangements)
print(f'Elapsed time: {round((time.time() - start), 2)}')
