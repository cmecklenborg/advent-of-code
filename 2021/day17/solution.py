
x_bounds = range(85, 146)
y_bounds = range(-163, -107)

# x_bounds = range(20, 31)
# y_bounds = range(-10, -4)


num_solutions = 0

for vx0 in range(500):
    for vy0 in range(-500, 500):

        x, y = 0, 0
        vx, vy = vx0, vy0
        for step in range(1000):
            x += vx
            y += vy

            if vx > 0:
                vx -= 1
            vy -= 1

            if x in x_bounds and y in y_bounds:
                num_solutions += 1
                break
            if x > x_bounds[-1] or y < y_bounds[0]:
                break

print(num_solutions)
