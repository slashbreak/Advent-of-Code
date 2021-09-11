import numpy
lines = open("input8.txt","r").readlines()
X = 50
Y = 6
count = 0
screen = numpy.zeros((Y,X), dtype=int)
#print screen

def rect(w, h):
    if w <= X and h <= Y:
        for i in range(h):
            for j in range(w):
                screen[i][j] = 1
#rect(3,4)

def rotate(axis, pos, shift):
    if axis == 'x':
        #columns
        temp = numpy.array([screen[i][pos] for i in range(Y)])
        temp = numpy.roll(temp, shift)
        for i in range(Y):
            screen[i][pos] = temp[i]
        #print temp
    elif axis == 'y':
        temp = numpy.array([screen[pos][i] for i in range(X)])
        temp = numpy.roll(temp, shift)
        for i in range(X):
            screen[pos][i] = temp[i]
    else: print "error"
#rotate('X', 1, 3)
#rotate('Y', 3, 1)

for l in lines:
    comm = l.split()
    # rect
    if comm[0] == 'rect':
        r = comm[1].split('x')
        rect(int(r[0]), int(r[1]))
    elif comm[1]== 'row':
        rotate('y', int(comm[2][2:]), int(comm[4]))
    elif comm[1] == 'column':
        rotate('x', int(comm[2][2:]), int(comm[4]))


for a in screen:
    t = ""
    for x in a:
        if x == 0: t+= " "
        else:

            t += str(x)
            count+=1
    print t
    print count

'''
11100100101110010010011001111001100111100111010000
10010100101001010010100101000010010100000010010000
10010100101001010010100001110010010111000010010000
11100100101110010010100001000010010100000010010000
10100100101010010010100101000010010100000010010000
10010011001001001100011001111001100111100111011110
'''
