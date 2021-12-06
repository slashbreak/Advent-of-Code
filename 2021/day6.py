#!/usr/bin/env python3

#AOC 2021 day 6
import copy
with open('input6') as f:
	lines = [x.strip() for x in f.readlines()]
fish = [int(x) for x in lines[0].split(',')]
buckets = {}
for i in range(9):
	buckets[i] = 0

for i in fish:
	buckets[i] += 1

def calculate_fish(steps, buckets):
	current_bucket = copy.deepcopy(buckets)
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
		buckets = copy.deepcopy(current_bucket)
	sums = 0
	for i in buckets.keys():
		sums+=buckets[i]
	return(sums)
	
print('Part 1: {}'.format(calculate_fish(80, buckets)))
print('Part 2: {}'.format(calculate_fish(256, buckets)))