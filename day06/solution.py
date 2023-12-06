import re
import math

with open('input.txt') as input:
    lines = input.read().splitlines()

wins = []

times = [int(t) for t in re.findall(r'\d+', lines[0])]
dists = [int(d) for d in re.findall(r'\d+', lines[1])]

for idx, time in enumerate(times):
    wins.append(0)
    for t in range(1, time):
        if t * (time - t) > dists[idx]:
            wins[idx] +=1

time = int(''.join(re.findall(r'\d+', lines[0])))
dist = int(''.join(re.findall(r'\d+', lines[1])))

wins_2 = 0

for t in range(1, time):
    if t * (time - t) > dist:
        wins_2 +=1

print(f'Part 1: {math.prod(wins)}')
print(f'Part 2: {wins_2}')
