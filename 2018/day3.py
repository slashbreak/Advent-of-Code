#! /usr/bin/env python3
from collections import defaultdict
d = defaultdict(int)

lines = []
with open('input3') as f:
    for l in f.readlines():
        lines.append( [int(n) for n in l.strip().split(' ')] )

def plot_rect(x,y,w,h):
    for i in range(y,y+h):
        for j in range(x,x+w):
            d[(i,j)] += 1
            
def is_lonely_rect(x,y,w,h):
    for i in range(y,y+h):
        for j in range(x,x+w):
            if d[(i,j)] > 1:
                return False
    return True

# PART 1    
for i in lines:
    _id, *dimensions = i
    plot_rect(*dimensions)
print('Part 1: %i' % sum([1 for i in d.values() if i > 1]))

# PART 2
final_id = ""
for i in lines:
    _id, *dimensions = i
    if is_lonely_rect(*dimensions):
        print('Part 2: %s' % _id)
        final_id = _id
        break
'''

# VISUALISATION        
from PIL import Image

img = Image.new('RGB',(1000,1000),'black')
for i in range(1000):
    for j in range(1000):
        if d[(i,j)] == 1:
            img.putpixel((i,j),(30,144,150))
        if d[(i,j)] == 2:
            img.putpixel((i,j),(20,70,90))
        if d[(i,j)] == 3:
            img.putpixel((i,j),(220,70,90))
        if d[(i,j)] >3:
            img.putpixel((i,j),(120,170,190))
            
ids,x,y,w,h = lines[final_id-1]
for i in range(y,y+h):
        for j in range(x,x+w):
            img.putpixel((i,j),(230,140,28))


img.show()
img.save('day3.jpg')
'''