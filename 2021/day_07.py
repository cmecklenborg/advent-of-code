with open('resources/day_07.txt') as f:
    line = f.readline().strip().split(',')

crabs = [int(c) for c in line]

min_pos = None
min_fuel = max(crabs)*len(crabs)**2

for pos in range(max(crabs)+1):

    fuel = sum([abs(c-pos)*(abs(c-pos)+1)/2 for c in crabs])
    if fuel < min_fuel:
        min_fuel = fuel
        min_pos = pos

print(f"Fuel: {min_fuel}, Position: {min_pos}")
