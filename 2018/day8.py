#! /usr/bin/env python3

'''
    A header, which is always exactly two numbers:
        The quantity of child nodes.
        The quantity of metadata entries.
    Zero or more child nodes (as specified in the header).
    One or more metadata entries (as specified in the header).


2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----
                     
'''
test = [int(x) for x in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')]
flat = []
with open('input8') as f:
    for l in f.readlines():
        for i in l.split(' '):
            flat.append(int(i))
        

#print(test)

from collections import defaultdict
#print(flat)
#flat = test
tree = {}
t = defaultdict(list)
count = 0
pos = 0
entsum = 0
def addNode(parent):
    global count
    global pos
    global entsum
    nodes = flat[pos]
    entries = flat[pos+1]
    pos += 2
    b = count
    count +=1
    for i in range(nodes):
        addNode(b)
    ent_list = []
    for i in range(entries):
        entsum += flat[pos]
        ent_list.append(flat[pos])
        pos+=1
    metasum = 0
    if nodes == 0:
        for h in ent_list:
            metasum += h
    else:
        metasum = 'bah'
    tree[b] = [nodes,ent_list, metasum]
    t[parent].append(b)
    
addNode('a')
print('Part 1: {}'.format(entsum))
#print(tree)
#print(t)
del t['a']
#print(t)

#tree {0: [2, [1, 1, 2], 'bah'], 1: [0, [10, 11, 12], 33], 2: [1, [2], 'bah'], 3: [0, [99], 99]}
#t {0: [1, 2], 2: [3]}

total = 0
a = 0
def summer(val):
    global a
    if tree[val][2] != 'bah':
        a += tree[val][2]
    else:
        kids = tree[val][1]
        for i in kids:
            if (i-1) >= 0 and (i-1) < len(t[val]):
                summer(t[val][i-1])
        
summer(0)
print('Part 2: {}'.format(a))
        

