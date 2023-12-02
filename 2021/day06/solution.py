from collections import Counter

with open('input.txt') as f:
    fish = f.readline().strip().split(',')

fish = Counter([int(f) for f in fish])

for day in range(256):

    new_fish = fish[0]
    for age in range(8):
        fish[age] = fish[age+1]
    fish[6] += new_fish
    fish[8] = new_fish

print(sum(fish.values()))
