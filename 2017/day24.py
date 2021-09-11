blobs = []
with open('input24.txt') as f:
    for l in f.readlines():
        blobs.append(l.strip().split('/'))

d = {}

def getEnd(start, blob):
    if blob[0] == start:
        return blob[1]
    else:
        return blob[0]

m = 0
le = 0
def solve(curr, currblobs, end, t, ll):
    global m
    global le
    if len(currblobs) <=0:
        return False
    for i in currblobs:
        if end in i:
            e = getEnd(end, i)
            a = currblobs[:]
            a.remove(i)
            t += int(i[0]) + int(i[1])
            if t > m:
                m = t
            if ll > le:
                le = ll
                print(le, t)
            #print(len(currblobs), i, t)
            #raw_input()
            c = i
            
            solve(c, a, e, t, ll+1)
            t -= int(i[0]) + int(i[1])
    return False
xx = blobs[:]
xx.remove(['0','4'])
solve(['0','4'], xx, '4', 4 ,0)
#print(m)

yy = blobs[:]
yy.remove(['0','47'])
m = 0
solve(['0','47'], yy, '47', 47, 0)
#print(m)

zz = blobs[:]
zz.remove(['0','29'])
m = 0
solve(['0','29'], zz, '29', 29, 0 )
#print(m)