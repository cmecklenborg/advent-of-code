from collections import defaultdict
import re
import sys

with open('input.txt') as input:
    lines = input.read().splitlines()

almanac = defaultdict(dict)
map = None

seeds = re.findall(r'\d+', lines[0])

for line in lines[1:]:
    header = re.match(r'[a-z -]+', line)
    if header:
        if header.group() == 'seed-to-soil map':
            map = 'seed'
        elif header.group() == 'soil-to-fertilizer map':
            map = 'soil'
        elif header.group() == 'fertilizer-to-water map':
            map = 'fert'
        elif header.group() == 'water-to-light map':
            map = 'water'
        elif header.group() == 'light-to-temperature map':
            map = 'light'
        elif header.group() == 'temperature-to-humidity map':
            map = 'temp'
        elif header.group() == 'humidity-to-location map':
            map = 'humidity'
    else:
        num_str = digits = re.findall(r'\d+', line)
        nums = [int(n) for n in num_str]
        if nums:
            dest, source, range_len = nums
            almanac[map][range(source, source + range_len)] = dest

    
# print(dict(almanac))

def source_to_dest(map: dict, source: int) -> int:
    for key in map:
        if source in key:
            return map[key] + source - key[0]
    return source


def part_1():
    lowest_loc = sys.maxsize
    for seed in seeds:
        source = int(seed)
        maps = ['seed', 'soil', 'fert', 'water', 'light', 'temp', 'humidity']
        for map in maps:
            dest = source_to_dest(almanac[map], source)
            source = dest

        lowest_loc = min(dest, lowest_loc)

    print(lowest_loc)


def part_2():
    lowest_loc = sys.maxsize
    for idx, s in enumerate(seeds[0::2]):
        seed_start = int(s)
        num_seeds = seeds[1::2][idx]
        seed_range = range(int(s), int(s) + int(num_seeds))
        for seed in seed_range:
            source = seed
            maps = ['seed', 'soil', 'fert', 'water', 'light', 'temp', 'humidity']
            for map in maps:
                dest = source_to_dest(almanac[map], source)
                source = dest

            lowest_loc = min(dest, lowest_loc)

    print(lowest_loc)

part_1()
