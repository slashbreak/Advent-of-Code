lines = open("input3.txt", "r").readlines()
lines[:] = [line.strip() for line in lines]
count = 0
'''for line in lines:
    a = line.split()
    a[:] = [int(x) for x in a]
    a[:] = sorted(a)
    if a[0]+a[1] > a[2]: 
        count += 1
        print a
    else: print "bah ", a
print " c ", count '''

for l in xrange(0,len(lines)-2, 3):
    a1 = lines[l].split()
    a1[:] = [int(x) for x in a1]
    b1 = lines[l+1].split()
    b1[:] = [int(x) for x in b1]
    c1 = lines[l+2].split()
    c1[:] = [int(x) for x in c1]
    a = [a1[0], b1[0],c1[0]]
    b = [a1[1], b1[1],c1[1]]
    c = [a1[2], b1[2],c1[2]]
    print a, b, c, 
    a[:] = sorted(a)
    b[:] = sorted(b)
    c[:] = sorted(c)
    if a[0]+a[1] > a[2]: 
        count += 1
    if b[0]+b[1] > b[2]: 
        count += 1
    if c[0]+c[1] > c[2]: 
        count += 1
print count
