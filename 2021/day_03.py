from collections import Counter
from copy import copy


with open('resources/day_03.txt') as f:
    all_lines = f.read().splitlines()

oxy_lines = copy(all_lines)

diag_len = len(all_lines[0])

for i in range(diag_len):
    if len(oxy_lines) == 1:
        break
    c = Counter([line[i] for line in oxy_lines])
    mode = '1' if c['1'] >= c['0'] else '0'
    oxy_lines = list(filter(lambda x: x[i] == mode, oxy_lines))
    pass

co2_lines = copy(all_lines)

for i in range(diag_len):
    if len(co2_lines) == 1:
        break
    c = Counter([line[i] for line in co2_lines])
    mode = '0' if c['0'] <= c['1'] else '1'
    co2_lines = list(filter(lambda x: x[i] == mode, co2_lines))

print(int(oxy_lines[0], 2) * int(co2_lines[0], 2))
