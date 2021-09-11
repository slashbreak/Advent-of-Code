
n = []
# 0 1 2
# 3 4 5
# 6 7 8
with open('input20.txt') as f:
    for l in f.readlines():
        a = [int(i) for i in l.strip().split(',')] + [0]
        n.append(a)
print(n)

for i in range(1000):
  for j in n:
    
    
    if j[9] != 1:
        for k in n:
            if k[9] != 1 and k != j:
                if j[0] == k[0] and j[1] == k[1] and j[2] == k[2]:
                    j[9] = 1
                    k[9] = 1
    j[3] += j[6]
    j[4] += j[7]
    j[5] += j[8]
    j[0] += j[3]
    j[1] += j[4]
    j[2] += j[5]
ab = 100000000000000
ind = -1
for i in n:
    a = (abs(i[0]) + abs(i[1]) + abs(i[2]))
    if a < ab:
        ab = a
        ind = n.index(i)

print('etst', ind)
print(n[0][9])

c = 0
for i in n:
    if i[9] != 1:
        c+= 1
print(c)