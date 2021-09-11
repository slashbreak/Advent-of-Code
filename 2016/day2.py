#numpad = [[1,2,3],
#          [4,5,6],
 #         [7,8,9]]

numpad = [[0,0,1,0,0],
          [0,2,3,4,0],
          [5,6,7,8,9],
          [0,"A","B","C",0],
          [0,0,"D",0,0]]
# 1 = [0][0]
# 2 = [0][1]
# 3 = [0][2]
final = ""
start = [2,0]
lines = open("input2.txt", "r").readlines()
#lines = ["ULL","RRDDD","LURDL","UUUUD"]
lines[:] = [line.strip() for line in lines]
#print len(lines)
for line in lines:
    print " le :", len(line), start
    ok = 0
    for ch in line:
        #print ch
        if ch == 'U':
            temp = [-1,0]
        elif ch == 'D':
            temp = [1,0]
        elif ch == 'L':
            temp = [0,-1]
        elif ch == 'R':
            temp = [0,1]
        else: print "READ ERROR"
            
        if (start[0] + temp[0]) not in [0,1,2,3,4] or (start[1] + temp[1]) not in [0,1,2,3,4]:
            print "skip", ch
        else: 
            if str(numpad[start[0]+temp[0]][start[1]+temp[1]]) != '0':
                ok = 1
        if ok== 1: 
            start[0] += temp[0]
            start[1] += temp[1]
            print "newpos : ", ch, numpad[start[0]][start[1]]
        ok = 0
        print start
    print numpad[start[0]][start[1]]
    final += str(numpad[start[0]][start[1]])
print final
    
