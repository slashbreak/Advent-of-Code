d = {}
rules = []
# populate dict with all orientations
def addRots(orig, target):    
    r0 = orig[:]
    r1 = zip(*r0[::-1])
    r2 = zip(*r1[::-1])
    r3 = zip(*r2[::-1])
    f0 = [x[::-1] for x in r0]
    f1 = [x[::-1] for x in r1]
    f2 = [x[::-1] for x in r2]
    f3 = [x[::-1] for x in r3]
    
    rots = []
    rots.append(r0)
    rots.append(r1)
    rots.append(r2)
    rots.append(r3)
    rots.append(f0)
    rots.append(f1)
    rots.append(f2)
    rots.append(f3)
    for i in rots:
        o = "".join(reduce(lambda x,y: x+y, i))
        d[o] = target
    
with open('input21.txt') as f:
    for l in f.readlines():
        a =  l.strip().split(' ')
        o, t = a[0].split('/'), a[1].split('/')
        addRots(o, "".join(t))

# split string back into separate columns
def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

start = ['.#.','..#','###']
x = 1
while x < 19:
    size = len(start[0])
    temp = []
    if size % 2 == 0:
        split = [0,0]
        pieceSize = size / 2
        lines = []
        for l in range(3*pieceSize + 2):
            lines.append([])
        for i in range(pieceSize):
            for j in range(pieceSize):
                split[0] = start[2*i][2*j :2*j+2]
                split[1] = start[2*i+1][2*j :2*j+2]
                
                temp = splitCount(d["".join(split)], 3)
                lines[3*i] += temp[0]
                lines[3*i+1] += temp[1]
                lines[3*i+2] += temp[2]

    elif size % 3 == 0:
        pieceSize = size / 3
        split = [0,0,0]
        lines = []
        for l in range(4*pieceSize+3):
            lines.append([])
        for i in range(pieceSize):
            for j in range(pieceSize):
                split[0] = start[3*i][3*j :3*j+3]
                split[1] = start[3*i+1][3*j :3*j+3]
                split[2] = start[3*i+2][3*j :3*j+3]
                
                temp = splitCount(d["".join(split)], 4)
                lines[4*i] += temp[0]
                lines[4*i+1] += temp[1]
                lines[4*i+2] += temp[2]
                lines[4*i+3] += temp[3]
    a = []
    for i in lines:
        a.append("".join(i))
    
    start = a
    print(x, sum(i.count('#') for i in start))
    x += 1
input()
        
        