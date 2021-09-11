
xyz = [0,0,0]
m = 0
with open('input11.txt') as f:
    for l in f.readlines():
        a = l.strip().split(',')
for c in a:
    
    if c == 'se':
        xyz[0] += 1
        xyz[1] -= 1

    if c == 'nw':
        xyz[0] -= 1
        xyz[1] += 1

    if c == 'n':
        xyz[1] += 1
        xyz[2] -= 1

    if c == 's':
        xyz[1] -= 1
        xyz[2] += 1

    if c == 'ne':
        xyz[0] += 1
        xyz[2] -= 1

    if c == 'sw':
        xyz[0] -= 1
        xyz[2] += 1
        
    b = max(abs(xyz[0]), abs(xyz[1]), abs(xyz[2]))
    if b > m:
        m = b
print(max(abs(xyz[0]), abs(xyz[1]), abs(xyz[2])))
print(m)
