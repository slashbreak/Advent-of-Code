jump = 370
l = [0]
pos = 0
le = 1
for i in range(1,50000001):
    pos = (pos +jump)%le+1
    #l.insert(pos, i)
    le += 1
    if pos == 1:
        print (i)
    #print(l)
