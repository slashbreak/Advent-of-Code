#! /usr/bin/env python3
from PIL import Image
pos_vel = []
with open('input10') as f:
    for l in f.readlines():
        a = l.strip().split()
        x,y,i,j = map(int,a)
        pos_vel.append([x,y,i,j])
print(pos_vel)

minx = min(x[0] for x in pos_vel)
maxx = max(x[0] for x in pos_vel)
miny = min(x[1] for x in pos_vel)
maxy = max(x[1] for x in pos_vel)

for i in range(10610,12000):
    img = Image.new('RGB',(1000,1000),'black')
    for j in pos_vel:
        x, y = j[0]+j[2]*i , j[1]+j[3]*i
        if x in range(1000) and y in range(1000):
            print(i)
        #break
            img.putpixel((x,y),(255,255,255))
    img.show()
    input()