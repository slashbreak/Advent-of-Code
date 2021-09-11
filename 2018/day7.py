#! /usr/bin/env python3

from networkx import *
graph = DiGraph()

with open('input7') as f:
    for n in f.readlines():
        l = n.strip().split(' ')
        graph.add_edge(l[1],l[7])
# PART 1
curr = [n for n,d in graph.in_degree() if d==0]
q = sorted(curr)
words = ''

while q:
    current = q.pop(0)
    words += current
    for i in graph.successors(current):
        add = True
        for j in graph.predecessors(i):
            if j not in words:
                add = False
        if add:
            q.append(i)
    q = sorted(q)
print('Part 1: {}'.format(words))

# PART 2
#elf structure -- [busy, node, timer]
elves = [[0,'_',0] for i in range(5)]
time_added = 60
q = sorted(curr)
words = ''
curr_time = 0
ok = True
while ok:
    temp = []
    for i in elves:
        if i[0] == 0 and q:
            i[0] = 1
            i[1] = q.pop(0)
            i[2] = (ord(i[1])-64) + time_added
    #print(elves, words,q, curr_time)
    for i in elves:
        if i[0] == 1:
            i[2] -= 1
            if i[2] == 0:
                temp += i[1]
                i[0] = 0 # not busy anymore
                for k in graph.successors(i[1]):
                    add = True
                    for j in graph.predecessors(k):
                        if j not in words and j not in temp:
                            add = False
                    if add:
                        q.append(k)
                i[1] = '_'
    #any nodes finished this tick have to be sorted alphabetically first
    sorted(temp)
    words += "".join(temp)
    
    #always sort the queue
    q = sorted(q)
    
    ok = False
    for a in elves:
        if a[0] == 1:
            ok = True
    if q:
        ok = True
        
    curr_time += 1
print('Part 2: {} {}'.format(curr_time, words))