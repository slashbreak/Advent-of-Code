#!/usr/bin/env python3

#AOC 2021 day 2
#Part 1
with open('input2') as f:
	lines = [x.strip() for x in f.readlines()]
	
pos = 0
depth = 0

for i in lines:
	direction, move = i.split()
	move = int(move)
	if direction == 'forward':
		pos += move
	elif direction == 'down':
		depth += move
	else:
		depth -= move

print("Part 1: {}".format(pos*depth))

#Part 2

pos = 0
depth = 0
aim = 0

for i in lines:
	direction, move = i.split()
	move = int(move)
	if direction == 'forward':
		pos += move
		depth += (aim * move)
	elif direction == 'down':
		aim += move
	else:
		aim -= move

print("Part 2: {}".format(pos*depth))