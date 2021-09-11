#! /usr/bin/env python3
lines = []
point_count = dict()
with open('input6') as f:
    for l in f.readlines():
        x = tuple([int(x) for x in l.strip().split(', ')])
        point_count[x] = 0
        lines.append(x)
#print(lines)
'''
from collections import defaultdict
from queue import Queue

grid = defaultdict(int)

coords_queue = []
for i in range(len(lines)):
    q = Queue()
    q.put(lines[i])
    coords_queue.append(q)

#print (coords_queue)

def neighbours(x,y):
    neighs = []
    neighs.append((x-1,y))
    neighs.append((x,y-1))
    neighs.append((x+1,y))
    neighs.append((x,y+1))
    return neighs
    
print(len(coords_queue))
'''

left_edge = min([x[0] for x in lines])
right_edge = max( [x[0] for x in lines])
top_edge = min([x[1] for x in lines])
bottom_edge = max([x[1] for x in lines])
region = 0

for x in range(left_edge,right_edge+1):
    for y in range(top_edge,bottom_edge+1):
        distmax = 9999999
        same = False
        curr = 0
        for a,b in lines:
            d = abs(a-x) + abs(b-y)
            curr += d
            if d == distmax:
                same = True
            if d < distmax:
                distmax = d
                cur_a, cur_b = a,b
                same = False
        if curr < 10000:
                region+=1
        if not same:
            if x in (left_edge,right_edge) or y in (top_edge,bottom_edge):
                point_count[(cur_a, cur_b)] = -999999
            else:
                point_count[(cur_a,cur_b)] +=1
print('Part 1: {}'.format(max(point_count.values())))
print('Part 2: {}'.format(region))




'''
count = 1
while count < 5:
    for i, node in enumerate(coords_queue):
        print('count ',i)
        #print(coords_queue[i])
        if isinstance(node,Queue):
            current = node.get()
        else:
            break
        #print(current)
        if current not in grid:
            grid[current] = count
        else:
            grid[current] = count
        for neigh in neighbours(*current):
            #print(i,current, neigh)
            if neigh[0] < left_edge or neigh[0] > right_edge or neigh[1] > bottom_edge or neigh[1] < top_edge:
                #don't add
                pass
                
            elif neigh not in grid:
                node.put(neigh)
                #print('adding',neigh)
            elif neigh in grid:
                if grid[neigh] != -1:
                    if grid[neigh] == count+1:
                        grid[current] = -1
                        print('ok')
                    else:
                        node.put(neigh)

                    
    count += 1
    #print(count)
    #print(coords_queue, len(coords_queue))
    coor_copy = coords_queue[:]
    for j in range(len(coor_copy)):
        if isinstance(coor_copy[j],int):
            pass
        elif (coor_copy[j].empty()):
            coords_queue[j] = 0
  
    #print('coords ', coords_queue, len(coords_queue))
    for i in range(top_edge,bottom_edge+1):
        for j in range(left_edge,right_edge+1):
            print(grid[(i,j)], end=',')
        print()
        '''