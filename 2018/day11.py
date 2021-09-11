#! /usr/bin/env python3

from collections import defaultdict
from operator import itemgetter

power_level = [[0 for x in range(301)] for y in range(301)]
serial = 5791

for y in range(1,301):
    for x in range(1,301):
        rack_id = x + 10
        power_level[x][y] = (rack_id * y + serial) * rack_id
        power_level[x][y] = int('000'+str(power_level[x][y])[-3])
        power_level[x][y] -= 5
        
sums = defaultdict(int)
for n in range(1,300):
    for y in range(1,301-n):
        for x in range(1,301-n):
            for i in range(n):
                for j in range(n):
                    sums[(x,y,n)] += power_level[x+i][y+j] 
    print(max(sums.items(), key=itemgetter(1))[0])