moves = [l.strip() for l in open("input3.txt")]
#print(moves)
dict = {"0 0":1}
index = [[0,0],[0,0]]
count = 0
print(len(moves[0]))
for i in moves[0]:
#for i in "^>v<":
    
    x = count % 2
    if i == '>':
        index[x][0] += 1
    if i == '<':
        index[x][0] -= 1
    if i == '^':
        index[x][1] += 1
    if i == 'v':
        index[x][1] -= 1
    count+=1    
    a = str(index[x][0]) + " " + str(index[x][1])
    print(a)
    dict[a] = 1
print(len(dict))
