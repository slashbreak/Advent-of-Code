input1 = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"

input2 = "R8, R4, R4, R8"
# 0,0
# 8,0
# 8,-4
# 4,-4
# 4,4

input3 = input1.split(", ")
position = [0,0]
visited = [[0,0]]
direc = [[0,1],[1,0],[0,-1],[-1,0]]
index = 0

for i in input3:
    if i[0] == 'R':
        index +=1
    else: 
        index -= 1
    amount = int(i[1:])
    for n in range(1,int(i[1:])+1):
        temp = [direc[index%4][0]*n,direc[index%4][1]*n]
        temp[0] += position[0]
        temp[1] += position[1]
        if temp in visited: print "here: ", temp
        visited.append(temp)
    
    vec = [x*amount for x in direc[index%4]]
    position[0] += vec[0]
    position[1] += vec[1]

    #temp = position[:]
    #if temp in visited: 
    #    print "Here: ", temp
    #else:
    #    visited.append(temp)
    #    print position
    
    #print i, position
print position[1]+position[0]*-1
