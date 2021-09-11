#! /usr/bin/env python3

from itertools import cycle
from itertools import count
import operator

class Train():
    train_id = count()
    def __init__(self, x, y, direction):
        self.pos = (x, y)
        self.direction = direction
        self.track_option = cycle([-1,0,1])
        self.t_id = next(Train.train_id)
        self.active = True

    def switch_dir(self, direction):
        self.direction = '^>v<'[('^>v<'.index(self.direction) + direction) % 4]

# Read the input and initialise trains        
tracks = [l.strip('\n') for l in open('input13').readlines()]
trains = []
for y in range(len(tracks)):
    for x in range(len(tracks[0])):
        if tracks[y][x] in '^>v<':
            trains.append(Train(x,y,tracks[y][x]))
    # Replace trains 'tile' with straight track
    tracks[y].replace('>','-').replace('<','-').replace('v','|').replace('^','|')
# Lookup to change grid position
offset = { '>':(1,0),'<':(-1,0),'v':(0,1),'^':(0,-1) }

p1done = False
p2done = False
while not p2done:
    for c, train in enumerate(trains):
        if not train.active:
            continue
        x,y = train.pos
        curr_track = tracks[y][x]
        if curr_track == '\\':
            if   train.direction == '>': train.direction = 'v'
            elif train.direction == '^': train.direction = '<'
            elif train.direction == '<': train.direction = '^'
            elif train.direction == 'v': train.direction = '>'
        elif curr_track == '/':
            if   train.direction == '>': train.direction = '^'
            elif train.direction == 'v': train.direction = '<'
            elif train.direction == '<': train.direction = 'v'
            elif train.direction == '^': train.direction = '>'
        elif curr_track == '+':
            train.switch_dir(next(train.track_option))
        # Update the train's position using the relevant offset
        train.pos = tuple(map(operator.add,train.pos, offset[train.direction]))
        # Every time a train moves, check whether it has crashed
        for i in range(len(trains)):
            if trains[i].pos == trains[c].pos and c != i and trains[i].active:
                trains[i].active = False
                trains[c].active = False
                if not p1done:
                    print('Part 1: Crash occured at {}'.format(trains[i].pos))
                    p1done = True
                if sum(t.active for t in trains) == 1:
                    for i in trains:
                        if i.active == 1:
                            print('Part 2: Last train at    {}'.format(i.pos))
                            p2done = True
                            break
    trains.sort(key = lambda z: z.pos)
    
    