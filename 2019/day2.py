#!/usr/bin/env python3

#AOC 2019 day 2
numbers_original = []    
with open('input2','r') as f:
    for l in f.readlines():
        for n in l.split(','):
            numbers_original.append(int(n))


#print(numbers)
'''
numbers_original = [1,0,0,0,99]
numbers = [2,3,0,3,99]
numbers = [2,4,4,5,99,0]
numbers = [1,1,1,4,99,5,6,0,99]
'''
#numbers_original = [1,0,0,0,99]


#part 1
#initialize new copy and set up starting pair
numbers = numbers_original[:]
numbers[1] = 12
numbers[2] = 2


for i in range(0,len(numbers),4):
    if numbers[i] == 1:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
    elif numbers[i] == 2:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
    elif numbers[i] == 99:
        print('die')
        break
    else:
        print('error: bad opcode')
        break

print(numbers[0])
#print(numbers)

## Part 2
target = 19690720

for i in range(0,100):
    for j in range(0,100):
        numbers = numbers_original[:]
        numbers[1] = i
        numbers[2] = j
        for n in range(0,len(numbers),4):
            if numbers[n] == 1:
                numbers[numbers[n+3]] = numbers[numbers[n+1]] + numbers[numbers[n+2]]
            elif numbers[n] == 2:
                numbers[numbers[n+3]] = numbers[numbers[n+1]] * numbers[numbers[n+2]]
            elif numbers[n] == 99:
                #print('die')
                break
            else:
                #print('error: bad opcode')
                break
        #print('her')
        #print(numbers)
        if numbers[0] == 19690720:
            print('found at {0}, {1}. 100 * {0} + {1} = {2}'.format(i,j, 100*i+j))