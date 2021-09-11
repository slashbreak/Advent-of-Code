#!/usr/bin/env python3

from collections import deque

puzzleinput = '51589'
puzzleinput = '01245'
puzzleinput = '92510'
puzzleinput = '846601'

recipes = [3,7]

elves = []
elves.append([recipes[0],0])
elves.append([recipes[1],1])

q = deque()
for c in puzzleinput:
    q.append(c)
    
count = -len(puzzleinput)+3
def check_recipe(s):
    global count
    for c in str(s):
        q.popleft()
        q.append(c)
        if "".join(q) == puzzleinput:
            return True
        count += 1
    return False

p1done = False
p2done = False
while not p2done:
    
    new_recipes = list(map(int,str(sum(x[0] for x in elves))))

    for r in new_recipes:
        recipes.append(r)
        if check_recipe(r):
            print('Part 2: {}'.format(count))
            p2done = True
            break
    for i in range(len(elves)):
        elves[i][1] = ( elves[i][1] + elves[i][0] + 1) % len(recipes)
        elves[i][0] = recipes[elves[i][1]]
    n = int(puzzleinput)
    if (len(recipes) > n + 10) and not p1done:
        s = ''.join(str(s) for s in recipes[n:n+10])
        print('Part 1: {}'.format(s))
        p1done = True

