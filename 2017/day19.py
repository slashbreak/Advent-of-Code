import string
import sys
sys.setrecursionlimit(200000)
letters = string.ascii_uppercase
pipes = []
with open('input19.txt') as f:
    for l in f.readlines():
        pipes.append(l.strip())
#print(pipes)
start = pipes[0].index('|')
rowlen = len(pipes[1])

#print(start)
#print(letters)
visited = [[0]*rowlen for p in range(len(pipes))]

#print(visited)
#print(rowlen)

finalStr = ""
c = 0
cross = 0
sym = "|"
def solve(row, col, symbol, d):
    global finalStr
    global c
    global cross
    global sym
    n = 1
    
    if row < 0 or row >= len(pipes[0]):
        return False
    if col < 0 or col >= len(pipes):
        return False
    if visited[row][col] == 1:
        if pipes[row][col] == '|' and d == -1:
            pass
        elif pipes[row][col] == '-' and d == 1:
            pass
        else:
            return False
    if pipes[row][col] == '.':
        return False
        
    print(row, col, pipes[row][col], sym, finalStr, d, c)
    
    if pipes[row][col] in letters:
        finalStr += pipes[row][col]
        if pipes[row][col] == 'Y':
            input()
    if pipes[row][col] == '|' and d == -1:
        if visited[row][col] != 1:
            n = 0
            cross -= 1
        #n = 0
    if pipes[row][col] == '-' and d == 1:
        if visited[row][col] != 1:
            n = 0
            cross -= 1
        #n = 0
    if pipes[row][col] == '+':
        d *= -1
    
    
    visited[row][col] = n
    if n == 1:
        cross += 1
        c += 1
    if d == -1:
        solve(row, col-1, sym, d)
        solve(row, col+1, sym, d)
    else:
        solve(row+1, col, sym, d)
        solve(row-1, col, sym, d)

    return True
print(pipes[0][start])
solve(0,start,'|', 1)
print('st', finalStr)
#print(visited)
print(c)
print(len(pipes), len(pipes[0]), len(visited), len(visited[0]))
print(c, cross, c-cross)

import math
field = open("input19.txt","r").read().split('\n')
x,y,d,end,steps = field[0].index("|"),0,1,False,1
while not end:
    end = True
    for i in range(d,d+4):
        dy, dx = int(math.sin(i*math.pi/2)),int(math.cos(i*math.pi/2))
        if y+dy >= 0 and y + dy < len(field) and x + dx >= 0 and x+dx < len(field[0]) and field[y+dy][x+dx] != ' ' and i%4 != (d+2)%4:
                d,end,steps,x,y = i,False,steps+1,x+dx,y+dy
                break
print(steps)

