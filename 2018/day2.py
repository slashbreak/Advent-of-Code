#! /usr/bin/env python3

from collections import Counter
from itertools import combinations

boxes = []
with open('input2.test') as f:
    for l in f.readlines():
        boxes.append(l.strip())
        
def checksum(box_id, num_to_find):
    duplicate_dict = Counter(box_id)
    if num_to_find in duplicate_dict.values():
        return 1
    return 0

twos = 0
threes = 0
for b in boxes:
    twos += checksum(b, 2)
    threes += checksum(b, 3)

print('Part 1: %i' % (twos*threes))

def p2():
    for a in range(len(boxes)):
        for b in range(a+1,len(boxes)):
            difference_count = 0
            final_id = ""
            for c in range(len(boxes[a])):
                if boxes[a][c] != boxes[b][c]:
                    difference_count += 1
                if difference_count > 1:
                    break
            if difference_count == 1:
                for c in range(len(boxes[a])):
                    if boxes[a][c] == boxes[b][c]:
                        final_id += boxes[a][c]
                #print('Part 2: ' + final_id)
                return 'Part 2: %s' % final_id
                
p2()