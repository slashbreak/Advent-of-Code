#! /usr/bin/env python3

from collections import deque
from itertools import cycle

SKIP_FACTOR = 23

with open('input9') as f:
    l = f.readline().strip().split(' ')
    players, final_score = int(l[0]), int(l[6])


def marbles(n, last):
    circle = deque([0])
    player_cycle = cycle(range(n))
    scores = [0] * n
    counter = 1
    while counter < last:
        current_player = next(player_cycle)
        if counter % SKIP_FACTOR == 0:
            circle.rotate(7)
            scores[current_player] += circle.pop() + counter
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(counter)
        counter += 1
    scores[current_player] += last 
    return max(scores)
    
print('Part 1: {}'.format(marbles(players,final_score)))
print('Part 2: {}'.format(marbles(players,final_score*100)))
