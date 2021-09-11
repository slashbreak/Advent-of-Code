#!/usr/bin/env python3

#AOC 2019 day 3
instructions = []
with open('input3','r') as f:
    for l in f.readlines():
        cable = []
        for a in l.strip().split(','):
            cable.append(a)
        instructions.append(cable)
#print (instructions)

#cable1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#cable2 = ['U62','R66','U55','R34','D71','R55','D58','R83'] # distance 159
#cable1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#cable2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'] # distance 135

def plot_route(instructions):
    direction_map = {'D':(0,-1),'U':(0,1),'L':(-1,0),'R':(1,0)}
    points = {}
    x = 0
    y = 0
    steps = 0
    for inst in instructions:
        direction = inst[0]
        amount = int(inst[1:])
        offset = direction_map[direction]
        for i in range(amount):
            steps += 1
            x += offset[0]
            y += offset[1]
            if not (x,y) in points:
                points[(x,y)] = steps
    return points
a = plot_route(instructions[0])
b = plot_route(instructions[1])
#a = plot_route(cable1)
#b = plot_route(cable2)
#print(a)
# all offset from (0,0)
def manhattan_dist(x, y):
    return abs(x) + abs(y)

def find_collisions(a, b):
    collisions = []
    shortest = 1000000000000000000
    collision_step_sum = 0
    shortest_step_sum = 100000000000000000
    for k, v in a.items():
        if k in b:
            collision_step_sum = 0
            collision_step_sum = a[k] + b[k]
            collisions.append(k)
            x, y = k #unpack coordinates
            d = manhattan_dist(x,y)
            print("collision at {0}. distance {1}".format(k, d))
            if d < shortest:
                print('new shortest {}'.format(d))
                shortest = d
            if collision_step_sum < shortest_step_sum:
                print('new shortest stepsum {}'.format(collision_step_sum))
                shortest_step_sum = collision_step_sum
                
    return shortest
shortest1 = find_collisions(a,b)
print('shortest distance: {}'.format(shortest1))


