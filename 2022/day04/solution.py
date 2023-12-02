with open('input.txt') as f:
    lines = f.readlines()

overlap = 0

for line in lines:
    a, b = line.strip().split(',')
    s1, e1 = map(int, a.split('-'))
    s2, e2 = map(int, b.split('-'))

    if (s2 <= s1 <= e2) or (s2 <= e1 <= e2) or (s1 <= s2 <= e1) or (s1 <= e2 <= e1):
        overlap += 1

print(overlap)
