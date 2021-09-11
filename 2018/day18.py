#!/usr/bin/env python3
from copy import deepcopy
grid = []
with open('input18') as f:
    for l in f.readlines():
        g = [x for x in l.strip()]
        grid.append(g)
for i in grid:
    print("".join(i))
print()
def adj(y,x):
    return [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]

grid1 = {}
for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid1[(row,col)] = grid[row][col]


count = 0
temp = deepcopy(grid1)

counts = set()
while count < 1000000000:

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            #print(row,col)
            trees = 0
            lumber = 0
            cleared = 0
            for a,b in adj(row,col):
                if a < 0 or a >= len(grid) or b < 0 or b >= len(grid):
                    pass
                else:
                    if grid1[(a,b)] == '.':
                        pass
                    elif grid1[(a,b)]  == '|':
                        trees += 1
                    else:
                        lumber += 1

            if grid1[(row,col)] == '.':
                if trees >= 3:
                    temp[(row,col)] = '|'
                else:
                    temp[(row,col)] = '.'
            elif grid1[(row,col)] == '|':
                if lumber >= 3:
                    temp[(row,col)] = '#'
                else:
                    temp[(row,col)] = '|'
            elif grid1[(row,col)] == '#':
                if lumber >= 1 and trees >= 1:
                    temp[(row,col)] = '#'
                else:
                    temp[(row,col)] = '.'
    grid1 = deepcopy(temp)
    #for j in range(len(grid)):
    #    for i in range(len(grid[0])):
    #        print(grid1[(j,i)],end='')
    #    print()
    woods = 0
    lumberyards = 0
    for x in grid1.values():
        if x == '|':
            woods += 1
        if x == '#':
            lumberyards +=1
    #print(count, woods, lumberyards, woods*lumberyards)
    if woods*lumberyards != 195305:
        counts.add(woods*lumberyards)
    else:
        print(count)
    #input()
    count += 1
    if count % 10000000 == 0:
        print('...')

    
woods = 0
lumberyards = 0
for x in grid1.values():
    if x == '|':
        woods += 1
    if x == '#':
        lumberyards +=1
print(woods, lumberyards, woods*lumberyards)