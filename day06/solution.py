import re
import math

with open('input.txt') as input:
    lines = input.read().splitlines()

def quad_solver(t, d) -> tuple:
    x1 = (t - math.sqrt(t**2 - 4*d))/2
    x2 = (t + math.sqrt(t**2 - 4*d))/2
    return (x1, x2)

# Part 1
wins = []

times = [int(t) for t in re.findall(r'\d+', lines[0])]
dists = [int(d) for d in re.findall(r'\d+', lines[1])]

for time, dist in zip(times, dists):
    x1, x2 = quad_solver(time, dist)
    min_hold, max_hold = math.floor(x1 + 1), math.ceil(x2 - 1)
    wins.append(max_hold - min_hold + 1)


# Part 2
time = int(''.join(re.findall(r'\d+', lines[0])))
dist = int(''.join(re.findall(r'\d+', lines[1])))

x1, x2 = quad_solver(time, dist)
min_hold, max_hold = math.floor(x1 + 1), math.ceil(x2 - 1)

print(f'Part 1: {math.prod(wins)}')
print(f'Part 2: {max_hold - min_hold + 1}')
