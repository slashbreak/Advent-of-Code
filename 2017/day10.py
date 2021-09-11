with open('input10.txt') as f:
    for l in f.readlines():
        line = [int(x) for x in l.strip().split(',')]

line2 = [3, 4, 1, 5]
knot = [x for x in range(256)]
index = 0
for i, c in enumerate(line):
    index %= 256
    knot = knot[index:] + knot[:index] # rotate
    knot = knot[:c][::-1] + knot[c:]
    knot = knot[-1*index:] + knot[:-1*index] # undo rotation
    index += c + i

print('p1', knot[0] * knot[1])

# part 2 
seq = [17, 31, 73, 47, 23]
with open('input10.txt') as f:
    for l in f.readlines():
        line = [ord(x) for x in l.strip()]
    line += seq

knot = [x for x in range(256)]
index, skip = 0, 0
for i in range(64):
    for c in line:
        index %= 256
        knot = knot[index:] + knot[:index] # rotate
        knot = knot[:c][::-1] + knot[c:]
        knot = knot[-1*index:] + knot[:-1*index] # undo rotation
        index += c + skip
        skip += 1

a = []
for i in range(16):
    a.append(knot[16*i:16*i+16])
    
tot = ""
for i in a:
    x = i[0]
    for j in range(1, 16):
        x ^= i[j]
    tot += format(x,'#04x')[2:]
print('p2', tot)

    
