with open('input.txt') as f:
    lines = f.readlines()

depths = [int(x.strip()) for x in lines]
# depths = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263
# ]

num_increases = 0
num_comparisons = 0
prev_sum = sum(depths[0:3])

for i in range(0, len(depths)-3):
    num_comparisons += 1
    curr_sum = prev_sum - depths[i] + depths[i+3]
    print(f"prev_sum: {prev_sum}, curr_sum: {curr_sum}")

    if curr_sum > prev_sum:
        num_increases += 1

    prev_sum = curr_sum

print(num_comparisons)
print(num_increases)