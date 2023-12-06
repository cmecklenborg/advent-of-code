from collections import defaultdict
import re


with open('input.txt') as input:
    lines = input.read().splitlines()

almanac = defaultdict(dict)
map = None

seed_str = re.findall(r'\d+', lines[0])
seeds = [int(s) for s in seed_str]
min_loc, max_loc = min(seeds), max(seeds)

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
            almanac[map][range(dest, dest + range_len)] = source
            min_loc = min(min_loc, dest)
            max_loc = max(max_loc, dest + range_len)

def dest_to_source(map: dict, source: int) -> int:
    for key in map:
        if source in key:
            return map[key] + source - key[0]
    return source


def part_1():
    for loc in range(min_loc, max_loc):
        dest = loc
        maps = ['humidity', 'temp', 'light', 'water', 'fert', 'soil', 'seed']
        for map in maps:
            source = dest_to_source(almanac[map], dest)
            dest = source 
        
        if source in seeds:
            print(loc)
            break

def part_2():

    seed_ranges = []
    for idx, s in enumerate(seeds[0::2]):
        ds = seeds[1::2][idx]
        seed_ranges.append(range(s, s + ds))

    for loc in range(min_loc, max_loc):
        if loc % 500000 == 0:
            print(f'{round(100*loc/max_loc, 2)} complete ...')

        dest = loc
        maps = ['humidity', 'temp', 'light', 'water', 'fert', 'soil', 'seed']
        for map in maps:
            source = dest_to_source(almanac[map], dest)
            dest = source
        
        if any([source in r for r in seed_ranges]):
            print(loc)
            break

part_1()
part_2()
