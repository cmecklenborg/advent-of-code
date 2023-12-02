with open('input.txt') as f:
    line = f.readline().strip()

print(line)

for i in range(14, len(line)):
    code = line[i-14:i]
    if len(code) == len (set(code)):
        print(i)
        break
