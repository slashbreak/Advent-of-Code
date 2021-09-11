#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
grid = set()
#grid[(500,0)] = '+'
with open('input17') as f:
    for line in f.readlines():
        a,b = line.strip().split(', ')
        if a[0] == 'y':
            y = int(a[2:])
            x1,x2 = b.split('..')
            x1 = int(x1[2:])
            x2 = int(x2)
            for i in range(x1,x2):
                grid.add((i,y))
        else:
            y = int(a[2:])
            x1,x2 = b.split('..')
            x1 = int(x1[2:])
            x2 = int(x2)
            for i in range(x1,x2+1):
                grid.add((y,i))
minx = min([x[0] for x in grid])
miny = min([x[1] for x in grid])
maxx = max([x[0] for x in grid])
maxy = max([x[1] for x in grid]) 

print(minx, miny, maxx, maxy)
'''
for y in range(miny, maxy+1):
    for x in range(minx-1,maxx+2):
        if (x,y) in grid:
            
            print(grid[(x,y)], end='')
        
        else:
            print('.',end='')
    print()
'''
# 0 -- moving
# 1 -- still
still, moving = set(), set()
def flow1(clay,bottom):
    
    def solve(x,y):
        if (x,y) in moving:
            return False
        moving.add((x,y))
        if y >= maxy:
            return False
        if (x,y+1) not in clay:
            solve(x,y+1)
        if (x,y+1) not in clay and (x,y+1) not in still:
            return False
            
        left_end = (x-1,y) in clay or solve(x-1,y)
        right_end = (x+1,y) in clay or solve(x+1,y)
        if left_end and right_end:
            left = (x-1,y)
            right =(x+1, y)
            still.add((x,y))
            while left in moving:
                still.add(left)
                left = (left[0] - 1, y)
            while right in moving:
                still.add(right)
                right = (right[0] + 1, y)
        return left_end or right_end
    solve(500,miny)
    
    return (len(moving), len(still))
    
print(flow1(grid,maxy))
'''
for y in range(miny, maxy+1):
    for x in range(minx-1,maxx+2):
        if (x,y) in grid:
            
            print('#', end='')
        elif (x,y) in still:
            print('^',end='')
        elif (x,y) in moving:
            print('~', end='')

        else:
            print(' ',end='')
    print()'''
 