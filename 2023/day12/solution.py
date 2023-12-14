import re
from itertools import product

file = 'input.txt'
with open(file) as input:
    lines = input.read().splitlines()

num_arrangements = 0

for line in lines:
    springs, buckets = line.split(' ')
    groups = [int(g) for g in re.findall(r'\d+', buckets)]

    op = '[.?]'
    br = '[#?]'

    lazy = f'^{op}*?' + f'{op}+?'.join([f'({br}{{{g}}})' for g in groups]) + f'{op}*?$'
    greedy = f'^{op}*' + f'{op}+'.join([f'({br}{{{g}}})' for g in groups]) + f'{op}*$'

    # print(f'Line {springs}')
    # print(f'Lazy regex {lazy}')
    # print(f'Greedy regex {greedy}')

    lazy_matches = re.search(fr'{lazy}', springs)
    greedy_matches = re.search(greedy, springs)
    lazy_starts = [lazy_matches.start(x) for x in range(1, len(lazy_matches.groups()) + 1)]
    greedy_starts = [greedy_matches.start(x) for x in range(1, len(greedy_matches.groups()) + 1)]

    arrangements = product(*[list(range(lazy_starts[x], greedy_starts[x] + 1)) for x in range(0, len(lazy_starts))])

    for arr in arrangements:
        valid_overlaps = all([arr[idx] > arr[idx-1] + groups[idx-1] for idx in range(1, len(arr))])
        bucket_chars = ''.join([springs[arr[idx]:arr[idx]+groups[idx]] for idx in range(0, len(arr))])
        between_chars = ''.join([springs[arr[idx-1] + groups[idx-1]:arr[idx]] for idx in range(1, len(arr))])

        if valid_overlaps and not '.' in bucket_chars and not '#' in between_chars:
            num_arrangements += 1

print(num_arrangements)
