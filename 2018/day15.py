#!/usr/bin/env python3
from collections import deque

class Elf():
    def __init__(self, y, x):
        self.attack = 15
        self.health = 200
        self.pos = (y,x)
        self.species = 'E'
        self.enemy = 'G'
        self.alive = True
class Goblin():
    def __init__(self, y, x):
        self.attack = 3
        self.health = 200
        self.pos = (y,x)
        self.species = 'G'
        self.enemy = 'E'
        self.alive = True
        
with open('input15') as f:
    grid = [list(a.strip()) for a in f.readlines()]
for j in range(len(grid)):
        for i in range(len(grid[0])):
            print(grid[j][i],end='')
        print()


elves = []
goblins = []

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'G':
            goblins.append(Goblin(row,col))
        elif grid[row][col] == 'E':
            elves.append(Elf(row,col))
e_count = len(elves)
#for i in elves:
#    print(i.pos)
#print()
#for i in goblins:
#    print(i.pos)


def adj(y,x):
    return [(y-1,x),(y,x-1),(y,x+1),(y+1,x)]

def bfs(start, unocc, goals):
    # traverse the cave in distance/reading order
    visited = [[0]*len(unocc[0]) for _t in range(len(unocc))]
    check = [[start]]
    visited[start[0]][start[1]] = 1
    while len(check):
        check_next = []
        while len(check):
            path = check.pop(-1) # pop from the end (faster)
            y,x = c = path[-1] # most recent coord
            if c in goals:
                return path # next move is the first step in this path
            for dy,dx in [(-1,0),(0,-1),(0,1),(1,0)]: # Reading order!
                if unocc[y+dy][x+dx] and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx]=1
                    check_next.append(path+[[y+dy,x+dx]])
        check = sorted(check_next, key=lambda path:path[-1], reverse=True)
        # sort by reading order of last position (thanks to /u/spencer8ab for pointing out the problem)
    return [] # no path to any goals

def find_enemy(my_species, start):
    goal = ''
    if my_species == 'G':
        goal = 'E'
    else:
        goal = 'G'
    paths = []
    frontier = deque()
    frontier.append(start)
    came_from = {}
    came_from[start] = None

    while frontier:
        current = frontier.popleft()
        #print('pos',current)
        y,x = current
        if grid[y][x] == goal:
            path = reconstruct_path(came_from,start,(y,x))
            if len(paths) > 0:
                if len(path) > len(paths[0]):
                    #print('aaa unsorted',paths)
                    paths.sort(key = lambda x: x[-2])
                    #print('aaa sorted',paths)
                    return paths
                else:
                    paths.append(path)
                    #print('aasaa usorted',paths)
                    paths.sort(key = lambda x: x[-2])
                    #print('aasaa sorted',paths)
            else:
                paths.append(path)
                paths.sort(key = lambda x: x[-2])
        for next in adj(y,x):
            v,u = next
            if next not in came_from:
                if grid[v][u] != '#' and grid[v][u] != my_species:
                    frontier.append(next)
                    came_from[next] = current
    #print('aaaaaa',paths)
    paths.sort(key = lambda x: x[-2])
    if len(paths) == 0:
        return [start]
    return paths

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    #path.append(start) # optional
    path.reverse() # optional
    return path

#print(find_enemy(goblins[0].species,goblins[0].pos))

count = 0
while True:
    creatures = []

    for i in goblins:
        if i.alive:
            creatures.append(i)
    for i in elves:
        if i.alive:
            creatures.append(i)
    
    creatures.sort(key = lambda x: x.pos)
    for bb, i in enumerate(creatures):
        if not i.alive:
            continue
        
        contin = False
        for z in creatures:
            if z.alive:
                if z.species == i.enemy:
                    if z.health > 0:
                        contin = True
        if not contin:
            #print('count is ', count)
            health = 0
            for q in creatures:
                if q.alive and q.health > 0:
                    health += q.health
            
            print('count is ', count, health, count*health)
            #input()
            break
        # ---- try to attack
        current_enemy = []
        for j in creatures:
            if j.alive and j.species == i.enemy:
                for next_pos in adj(*i.pos):
                    y,x = next_pos
                    if (y,x) == j.pos:
                        current_enemy.append([j.health, j.pos])

        if current_enemy:
            #print(current_enemy)
            current_enemy.sort()
            #print(current_enemy)
            #print(i.pos,current_enemy)
            attack = current_enemy[0][1]
            #print(attack)
            for n in creatures:
                if n.pos == attack:
                    #print('ok',n.pos,n.health)
                    n.health -= i.attack
                    if n.health <= 0:
                        n.alive = False
                        b,a = n.pos
                        grid[b][a] = '.'
                    #print('{} attacked {}. health at {}'.format((i.species,i.pos,i.health), n.pos,n.health))
        else:
        
            # --------- move
            #print('a',i.pos)
            near = adj(*i.pos)
            #print('b',i.pos)
            move = True

            if move:
                position = find_enemy(i.species,i.pos)
                #print(position, len(position), 'herere', i.pos)
                if position[0] == i.pos:
                    print(i.pos, 'Did not move')
                else:
                    print('{} at {} sees {} targets. moving to {}'.format(i.species,i.pos,len(position), position[0][-1]))

                    if len(position) > 1:
                        for gg in position:
                            print(gg)
                    #print(i.pos,'moving to: ',end='')
                    prev_pos = i.pos
                    y,x = prev_pos
                    grid[y][x] = '.'
                    #print('aaa',position[0])
                    i.pos = position[0][0]
                    y,x = i.pos
                    grid[y][x] = i.species
            current_enemy = []
            for j in creatures:
                if j.alive and j.species == i.enemy:
                    for next_pos in adj(*i.pos):
                        y,x = next_pos
                        if (y,x) == j.pos:
                            current_enemy.append([j.health, j.pos])

            if current_enemy:
                #print(current_enemy)
                current_enemy.sort()
                #print(current_enemy)
                #print(i.pos,current_enemy)
                attack = current_enemy[0][1]
                #print(attack)
                for n in creatures:
                    if n.pos == attack:
                        #print('ok',n.pos,n.health)
                        n.health -= i.attack
                        if n.health <= 0:
                            n.alive = False
                            b,a = n.pos
                            grid[b][a] = '.'#print(i.pos)
    print('After round {}'.format(count))
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            print(grid[j][i],end='')
        print()
    
    #input()
    goblins[:] = [x for x in goblins if x.alive]
    elves[:] = [x for x in elves if x.alive]
    if len(goblins) == 0 or len(elves)== 0:
        health = 0
        for q in goblins:
            if q.alive and q.health > 0:
                health += q.health
        for q in elves:
            if q.alive and q.health > 0:
                health += q.health
        
        print('counasdast is ', count, health, count*health)
        break
    count += 1
print(e_count, len(elves))
                