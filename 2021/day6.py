#!/usr/bin/env python3

#AOC 2021 day 6
import copy
with open('input6') as f:
	lines = [x.strip() for x in f.readlines()]
fish = [int(x) for x in lines[0].split(',')]
fish = [3,4,3,1,2]
buckets = []
for i in range(9):
	buckets.append(0)

for i in fish:
	buckets[i] += 1

def calculate_fish(steps, buckets):
	current_bucket = buckets[:]
	for i in range(steps):
		current_bucket[8] = buckets[0]
		current_bucket[7] = buckets[8]
		current_bucket[6] = buckets[0] + buckets[7]
		current_bucket[5] = buckets[6]
		current_bucket[4] = buckets[5]
		current_bucket[3] = buckets[4]
		current_bucket[2] = buckets[3]
		current_bucket[1] = buckets[2]
		current_bucket[0] = buckets[1]
		buckets = current_bucket[:]
	sums = 0
	for i in buckets:
		sums+=i
	return(sums)
	
print('Part 1: {}'.format(calculate_fish(80, buckets)))
print('Part 2: {}'.format(calculate_fish(67108864 , buckets)))