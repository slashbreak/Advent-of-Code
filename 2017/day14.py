#"hwlqcszp-"
import sys
#sys.setrecursionlimit(25000)
seq = [17, 31, 73, 47, 23]
lns = []
xxx = "xlqgujun"
for l in range(128):
    ln = "hwlqcszp-" + str(l)
    line = [ord(x) for x in ln]
    line += seq
    lns.append(line)
def knotty(line):
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
    t = ""
    for i in a:
        x = i[0]
        for j in range(1, 16):
            x ^= i[j]
        tot += format(x,'#04x')[2:]

        t += format(x,'#010b')[2:]
        #print(x, format(x,'#010b')[2:])
    
    #print(line)
    #print(tot, len(tot))
    #print(t, len(t))
    return (t)
grid = []
count = 0
for x in lns:
    a = knotty(x)
    #if len(a) != 128:
    #    print 'err'
    for i in a:
        if i == '1':
            count += 1
    grid.append(a)
print(count)
#for i in grid:
#    print (grid)
regions = []

visited = [ [0]*128 for _ in range(128) ]
colours = [ [-1]*128 for _ in range(128) ]
#print visited[127]
color = 0
def solve(row, col):
    #global visited
    #global grid
    global count
    global regions
    if row < 0 or row > 127:
        return False
    if col < 0 or col > 127:
        return False
    if grid[row][col] == '0':
        visited[row][col] = 1
        return False
    if visited[row][col] == 1:
        return False

    visited[row][col] = 1
    colours[row][col] = color
    solve(row, col+1)
    solve(row+1, col)
    solve(row, col-1)
    solve(row-1, col)

    return True
c = 0
for i in range(128):
    for j in range(128):
        a = solve(i, j)
        if a:
            c += 1
            color += 1
print(c)
#for i in range(256):
    #print(format(i,'#04x')[2:], format(i,'#010b')[2:])
import random
co = []
cd = [(244,40,9),(92,222,14),(84,32,221),(112,61,92)]
for i in range(c):
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    co.append((r,g,b))
from PIL import Image
img = Image.new('RGB', (128,128), "black")
pixels = img.load()

#print (co)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if colours[i][j] != -1:
            pixels[i,j] = co[colours[i][j]]
            pixels[i,j] = cd[(colours[i][j])%4]
img = img.resize((1024,1024))
#img.save('out.png')
img.show()

