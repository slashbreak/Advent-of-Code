lists = []
amount = 0
ribbon = 0
with open("input2.txt") as f:
    for line in f.readlines():
        lists.append(line.strip().split('x'))

for a in lists: 
    l,w,h = sorted(map(int, a))
    amount += 2*l*w + 2*l*h + 2*w*h + (min(l*w, l*h, w*h))
    ribbon += l*w*h
    ribbon += l+l+w+w
print(amount)
print(ribbon)