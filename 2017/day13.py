import copy
d1 = {}
d2 = {}
for i in range(100):
    d1[i] = [-1, -2, -3]
with open('input13.txt') as f:
    for l in f.readlines():
        a = l.strip().split()
        d1[int(a[0])] = [int(a[1]), 0, 1] # range, pos, dir
        d2[int(a[0])] = int(a[1])
d = copy.deepcopy(d1)

def delay(n):

    d = copy.deepcopy(d1)
    for j in range(n):    
        for i in range(100):    
            if d[i][2] == 1:
                if (d[i][1] + 1) >= (d[i][0]):
                    d[i][2] = -1
                    d[i][1] -= 1
                else:
                    d[i][1] += 1
            elif d[i][2] == -1:
                if (d[i][1] -1) < 0:
                    d[i][2] = 1
                    d[i][1] += 1
                else:
                    d[i][1] -= 1

def go():
    total = 0
    caught = False
    for j in range(100):

        if d[j][1] == 0:
            caught = True
            total += (j*(d[j][0]))
        for i in range(100):    
            if d[i][2] == 1:
                if (d[i][1] + 1) >= (d[i][0]):
                    d[i][2] = -1
                    d[i][1] -= 1
                else:
                    d[i][1] += 1
            elif d[i][2] == -1:
                if (d[i][1] -1) < 0:
                    d[i][2] = 1
                    d[i][1] += 1
                else:
                    d[i][1] -= 1

    return caught
x= False
z = 0

delays = 0
safe = False
totals = 0
while not safe:
    safe = True
    for key, val in d2.items():
        if (delays + key) % ((val*2)-2) == 0:
            if delays == 0:
                totals += key*val
            safe = False
    #print('')
    if safe:
        print(delays)
    if delays == 0:
        print(totals)    
    delays += 1
print(z)
