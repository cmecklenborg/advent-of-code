from collections import Counter, defaultdict

with open('input.txt') as f:
    old_poly = f.readline().strip()
    f.readline()
    lines = f.read().splitlines()

old_pair_count = defaultdict(int)
for idx in range(len(old_poly)-1):
    pair = old_poly[idx:idx + 2]
    old_pair_count[pair] += 1
last_char = old_poly[-1]

mapping = {}

for line in lines:
    start, fin = line.split(' -> ')
    mapping[start] = fin

for _ in range(40):
    new_pair_count = defaultdict(int)
    for k, v in old_pair_count.items():
        p1 = k[0]
        p2 = mapping[k]
        p3 = k[1]
        new_pair_count[p1+p2] += v
        new_pair_count[p2+p3] += v

    old_pair_count = new_pair_count

c = Counter()
for k, v in new_pair_count.items():
    c[k[0]] += v
c[last_char] += 1

most_common = c.most_common()

print(most_common[0][1]-most_common[-1][1])
