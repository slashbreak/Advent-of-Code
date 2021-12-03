#!/usr/bin/env python3

#AOC 2021 day 3

with open('input3') as f:
	lines = [x.strip() for x in f.readlines()]

transposed = [''.join(s) for s in zip(*lines)]
b_data = "".join(['0' if (x.count('0') > x.count('1')) else '1' for x in transposed])

gamma_rate = int(b_data, 2)
bitmask = int('1'*len(b_data),2)
consumption = bitmask ^ int(b_data,2)

print('Part 1: {}'.format(gamma_rate*consumption))

#Part 2

new_lines = lines[:]
for i in range(len(transposed)):
	if len(new_lines) == 1:
		oxy_gen_rating = int(new_lines[0],2)
		break
	transposed = [''.join(s) for s in zip(*new_lines)]
	a = transposed[i].count('1') >= transposed[i].count('0')
	new_lines = [x for x in new_lines if x[i] == str(int(a))]

#DIRTY CODE REUSE
new_lines = lines[:]
for i in range(len(transposed)):
	if len(new_lines) == 1:
		co2_scrubber_rating = int(new_lines[0],2)
		break
	transposed = [''.join(s) for s in zip(*new_lines)]
	a = transposed[i].count('1') >= transposed[i].count('0')
	new_lines = [x for x in new_lines if not (x[i] == str(int(a)))]
	
print('Part 2: {}'.format(co2_scrubber_rating * oxy_gen_rating))
	