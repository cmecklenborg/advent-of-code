with open('input.txt') as f:
    lines = f.read().splitlines()

octs = []
for line in lines:
    octs.append([int(x) for x in line])

max_x, max_y = 10, 10
num_flashes = 0


def process_flash(octs, x, y):
    for y2 in range(max(y-1, 0), min(y+2, max_y)):
        for x2 in range(max(x-1, 0), min(x+2, max_x)):
            if x2 == x and y2 == y:
                continue
            if octs[y2][x2]:
                octs[y2][x2] += 1


for step in range(1000):

    for y in range(max_y):
        for x in range(max_x):
            octs[y][x] += 1

    flashing = True
    while flashing:
        flashing = False
        for y in range(max_y):
            for x in range(max_x):
                if octs[y][x] and octs[y][x] > 9:
                    flashing = True
                    num_flashes += 1
                    process_flash(octs, x, y)
                    octs[y][x] = None

    if not any(any(oct) for oct in octs):
        print(f"Synchronized Step: {step+1}")
        break

    for y in range(max_y):
        for x in range(max_x):
            if octs[y][x] is None:
                octs[y][x] = 0
