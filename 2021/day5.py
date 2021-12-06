#!/usr/bin/env python3

#AOC 2021 day 5

with open('input5') as f:
	lines = [x.strip() for x in f.readlines()]
grid = {}
for line in lines:
	a,b = line.split(' -> ')
	a = a.split(',')
	b = b.split(',')
	x1 =int(a[0])
	x2 = int(b[0])
	y1 =int(a[1])
	y2 =int(b[1])
	if x1==x2 or y1==y2:
		for i in range(min(x1,x2),max(x1,x2)+1):
			for j in range(min(y1,y2),max(y1,y2)+1):
				if (j,i) in grid:
					grid[(j,i)] += 1
				else:
					grid[(j,i)] = 1
	else:
		m = int((y2-y1)/(x2-x1))
		if min(y1,y2) == y1:
			x = x1
		else:
			x = x2
		for i in range(min(y1,y2),max(y1,y2)+1):
			if (i,x) in grid:
				grid[(i,x)] += 1
			else:
				grid[(i,x)] = 1
			x+=m
	


sum = 0
for key in grid.keys():
	if grid[key] > 1:
		sum+=1
print(sum)
'''
for i in range(11):
	for j in range(11):
		if (i,j) not in grid:
			print('0',end='')
		else:
			print(grid[(i,j)],end='')
	print()	
'''