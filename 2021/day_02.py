with open('resources/day_02.txt') as f:
    lines = f.readlines()

commands = [x.strip().split(' ') for x in lines]

horz = 0
depth = 0
aim = 0

for command in commands:
    dir, delta = command[0], int(command[1])

    if dir == "forward":
        horz += delta
        depth += aim*delta
    elif dir == "down":
        aim += delta
    elif dir == "up":
        aim -= delta

print(horz, depth, horz*depth)
