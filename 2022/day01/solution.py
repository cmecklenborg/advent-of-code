with open('input.txt') as f:
    lines = f.readlines()

calories = {0: 0}
idx = 0

for line in lines:
    if line.strip() == '':
        idx += 1
        calories[idx] = 0
    else:
        calories[idx] += int(line.strip())

print(sum(sorted(calories.values(), reverse=True)[0:3]))
