old = []
count = 0

with open('input6.txt') as f:
    for l in f.readlines():
        blocks = [int(x) for x in l.strip().split('\t')]

while blocks not in old:
    old.append(blocks[:])
    count += 1
    index = blocks.index(max(blocks))
    for i in range(max(blocks)):
        blocks[index] -= 1
        blocks[(index+1+i) % len(blocks)] += 1
        
print (count, count - old.index(blocks)) # (part1, part2)
