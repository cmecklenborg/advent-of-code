from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()

filepath = []
sizes = defaultdict(int)

prev = None
curr = '/'
folders = {}

for line in lines:
    # Command
    if line[0] == '$':
        cmd = line[2:]
        if cmd == 'cd ..':
            filepath.pop()
        elif 'cd' in cmd:
            filepath.append(cmd.split()[-1])
    # File sizes
    else:
        size, _ = line.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i+1])] += size

# define constants
total_space = 70000000
update_size = 30000000
used_space = sizes['/']
free_space = total_space - used_space
space_needed = update_size - free_space

dirs = [val for val in sizes.values() if val >= space_needed]

print(min(dirs))
