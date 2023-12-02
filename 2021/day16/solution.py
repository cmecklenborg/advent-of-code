import math

with open('input.txt') as f:
    lines = f.read().splitlines()

versions = 0


def process_packet(n):
    global versions
    V = bin[n:n+3]
    T = bin[n+3:n+6]
    type = int(T, 2)
    n += 6

    versions += int(V, 2)

    # Literal number
    if type == 4:
        num = ''
        while True:
            group = bin[n:n+5]
            num += group[1:5]
            n += 5
            if group[0] == '0':
                break
        print(f"Literal number: {int(num, 2)}")
        return n, int(num, 2)
    # Operator
    else:
        packets = []
        I = bin[n]
        n += 1
        if int(I, 2) == 0:
            # Length of sub-packets
            L = bin[n:n + 15]
            n += 15
            packet_length = int(L, 2)
            target_n = n + packet_length
            while n < target_n:
                n, v = process_packet(n)
                packets.append(v)
        else:
            # Number of sub-packets
            L = bin[n:n + 11]
            n += 11
            packets_remaining = int(L, 2)
            while packets_remaining:
                n, v = process_packet(n)
                packets.append(v)
                packets_remaining -= 1

        if type == 0:
            print(f"Sum of {packets}")
            return n, sum(packets)
        elif type == 1:
            print(f"Prod of {packets}")
            return n, math.prod(packets)
        elif type == 2:
            print(f"Min of {packets}")
            return n, min(packets)
        elif type == 3:
            print(f"Max of {packets}")
            return n, max(packets)
        elif type == 5:
            print(f"Greater than of {packets}")
            return n, 1 if packets[0] > packets[1] else 0
        elif type == 6:
            print(f"Less than of {packets}")
            return n, 1 if packets[0] < packets[1] else 0
        elif type == 7:
            print(f"Equal to of {packets}")
            return n, 1 if packets[0] == packets[1] else 0


hex = lines[0]
bin = format(int(hex, 16), f"0{len(hex) * 4}b")

n, val = process_packet(0)
print(val)
