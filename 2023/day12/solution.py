import re


file = 'input.txt'
with open(file) as input:
    lines = input.read().splitlines()


def valid_count(record, groups):
    # print(f'Evaluating record {record} with groups {groups}')
    if not groups:
        return 0 if '#' in record else 1

    min_start = 0
    max_start = len(record) - sum(groups) - len(groups) + 1
    if '#' in record:
        max_start = min(max_start, record.index('#'))

    size = groups[0]
    valid = 0
    for idx in range(min_start, max_start + 1):
        this_chunk = record[idx:idx+size]
        next_chunk = record[idx+size:]
        # print(f'This chunk {this_chunk} next chunk {next_chunk}')
        if all(c in '#?' for c in this_chunk) and (len(next_chunk) == 0 or next_chunk[0] in '.?'):
            args = (next_chunk[1:], tuple(groups[1:]))
            if args not in cache:
                cache[args] = valid_count(*args)
            valid += cache[args]

    return valid


cache = {}


def part_1(lines):
    arrangements = 0
    for line in lines:

        record, buckets = line.split(' ')
        groups = [int(g) for g in re.findall(r'\d+', buckets)]
        arrangements += valid_count(record, groups)

    print(f'Part 1: {arrangements}')


def part_2(lines):
    arrangements = 0
    for line in lines:
        record, buckets = line.split(' ')
        groups = [int(g) for g in re.findall(r'\d+', buckets)]
        folded_record = '?'.join([record for _ in range(5)])
        folded_groups = groups*5
        arrangements += valid_count(folded_record, folded_groups)

    print(f'Part 2: {arrangements}')


part_1(lines)
part_2(lines)
