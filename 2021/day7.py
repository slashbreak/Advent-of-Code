#!/usr/bin/env python3
#AOC 2021 day 7

from math import floor

with open('input7') as f:
	lines = [int(x) for x in f.read().strip().split(',')]

median = sorted(lines)[len(lines)//2]
mean = floor((sum(lines)/len(lines)))
p1 = sum([abs(x-median) for x in lines])
p2 = int(sum([(abs(x-mean)*(abs(x-mean)+1)/2) for x in lines]))

print('Part 1: {}'.format(p1))
print('Part 2: {}'.format(p2))
