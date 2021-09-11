initial = []
with open('input22.txt') as f:
    for l in f.readlines():
        initial.append(l.strip())

grid = {}

def makeKey(a, b):
    return (str(a) + " " + str(b))

#initial = [['a','b','c'],['d','e','f'],['g','h','i']]
initLen = (len(initial[0])-1) / 2
for x in range(len(initial)):
    for y in range(len(initial)):
        grid[makeKey(x-initLen, y - initLen)] = initial[x][y]

#print(grid[makeKey(0,0)])
#print(grid)
#for i in initial:
#    print(i)
x, y = 0, 0

directions = [(-1,0),(0,1),(1,0),(0,-1)]
chg = {'#':('F',1),'.':('W',-1),'W':('#',0),'F':('.',2)}
dPos = 0
burstCause = 0
i = 0
#print chg['#'][1]
while i < 10000000:
    key = makeKey(x, y)
    
    if key not in grid:
        grid[key] = '.'
    
    current = grid[key]
    '''if current not in chg:
        print('die')
    else:
        grid[key] = chg[current][0]
        dPos += chg[current][1]
    if current == 'W':
        burstCause += 1
    '''
       
    if current == '#':
        grid[key] = 'F'
        dPos += 1
    elif current == 'F':
        grid[key] = '.'
        dPos += 2        
    elif current == '.':
        grid[key] = 'W'
        dPos -= 1
    elif current == 'W':
        grid[key] = '#'
        burstCause += 1

    dPos %= 4
    x += directions[dPos][0]
    y += directions[dPos][1]
    
    i += 1

print(burstCause)
'''
print(len(grid))
curr = 0
for i in grid.keys():
    a = int(i.split(' ')[1])
    if a < curr:
        curr = a
print curr

for x in range(-171, 203):
    a = ""
    for y in range(-203, 163):
        key = makeKey(x, y)
        
        if key in grid:
            a += grid[key]
        else:
            a += '.'
    print(a)
'''    