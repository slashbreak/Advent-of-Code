#!/usr/bin/env python3

#AOC 2021 day 1

with open('input1') as f:
	lines = [int(x.strip()) for x in f.readlines()]

# Part 1
# For each number, if it is greater than the previous number add to a counter

part1_count = 0
current = lines[0]
for i in lines[1:]:
	if i > current:
		part1_count += 1
	current = i

print("Part 1: {}".format(part1_count))

# Part 2
# For each consecutive 3 numbers, if their sum is greater than the previous sum, add to the counter
'''
199  A      			sumA(199,200,208) = 607
200  A B    			sumB(200,208,210) = 618
208  A B C  			sumB > sumA, so increase count
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
'''

part2_count = 0
current_sum = sum(lines[i] for i in range(3))

for i in range(1,len(lines)-2):
	next_sum = sum(lines[y] for y in range(i,i+3))
	if next_sum > current_sum:
		part2_count += 1
	current_sum = next_sum
	
print("Part 2: {}".format(part2_count))