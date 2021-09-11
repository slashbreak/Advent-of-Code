#!/usr/bin/env python3

#AOC 2019 day 5
numbers_original = []    
with open('input5','r') as f:
    for l in f.readlines():
        for n in l.strip().split(','):
            numbers_original.append(n)



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
#numbers = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#numbers = [101,-1,7,7,4,7,1105,11,0,99]
print(numbers)
#numbers[1] = 12
#numbers[2] = 2

#numbers = [1101,100,-1,4,0]

def int_add(modes, buf, index):
    if modes[0] == '0':
        a = buf[int(buf[index+1])]
        #print('a',a)
    else:
        a = buf[index+1]
    if modes[1] == '0':
        b = buf[int(buf[index+2])]
        #print('b',b)
    else:
        b = buf[index+2]
    buf[int(buf[index+3])] = str(int(a)+int(b))
    #print('c',buf[index+3])
    
def int_mul(modes, buf, index):
    if modes[0] == '0':
        a = buf[int(buf[index+1])]
    else:
        a = buf[index+1]
    if modes[1] == '0':
        b = buf[int(buf[index+2])]
    else:
        b = buf[index+2]
    
    buf[int(buf[index+3])] = str(int(a)*int(b))

def int_input(modes, buf, index):
    a = input('Input: ')
    buf[int(buf[index+1])] = a

def int_output(modes, buf, index):
    if modes[0] == '0':
        print('Output: {}'.format(buf[int(buf[index+1])]))
    else:
        print('Output_imm: {}'.format(buf[index+1]))

def int_jmp_true(modes, buf, index):
    c = 'bad'
    if modes[0] == '0':
        a = buf[int(buf[index+1])]
    else:
        a = buf[index+1]
    if modes[1] == '0':
        b = buf[int(buf[index+2])]
    else:
        b = buf[index+2]
    if int(a) != 0:
        c = b
    print('c', c)
    return c
def int_jmp_false(modes, buf, index):
    c = 'bad'
    if modes[0] == '0':
        a = buf[int(buf[index+1])]
    else:
        a = buf[index+1]
    if modes[1] == '0':
        b = buf[int(buf[index+2])]
    else:
        b = buf[index+2]
    if int(a) == 0:
        c = b
    print('c', c)
    return c
def int_less_than(modes, buf, index):
    if modes[0] == '0':
        a = buf[int(buf[index+1])]
    else:
        a = buf[index+1]
    if modes[1] == '0':
        b = buf[int(buf[index+2])]
    else:
        b = buf[index+2]
    if (int(a) < int(b)) :
        buf[int(buf[index+3])] = 1
    else:
        buf[int(buf[index+3])] = 0
def int_equals(modes, buf, index):
    if modes[0] == '0':
        a = buf[int(buf[index+1])]
    else:
        a = buf[index+1]
    if modes[1] == '0':
        b = buf[int(buf[index+2])]
    else:
        b = buf[index+2]
    if (int(a) == int(b)) :
        buf[int(buf[index+3])] = 1
    else:
        buf[int(buf[index+3])] = 0


inst_counter = 0
instruction = str(numbers[inst_counter])[-1:]
print(instruction)
while instruction != '9':
    
    instruction = str(numbers[inst_counter])[-1:]
    modes = str(numbers[inst_counter])[:-2][::-1] + '0000' # reverse mode bits and pad with 0's
    
    print(inst_counter, instruction, modes)
    print(numbers[inst_counter:inst_counter+5])
    #input()
    if instruction == '1':
        #add
        int_add(modes, numbers, inst_counter)
        inst_counter += 4
    elif instruction == '2':
        #mult
        int_mul(modes,numbers,inst_counter)
        inst_counter += 4
    elif instruction == '3':
        #input
        int_input(modes,numbers,inst_counter)
        inst_counter += 2
    elif instruction == '4':
        #output
        int_output(modes,numbers,inst_counter)
        inst_counter += 2
    elif instruction == '5':
        ans = int_jmp_true(modes, numbers, inst_counter)
        if ans != 'bad':
            inst_counter = int(ans)
        else:
            inst_counter += 3
    elif instruction == '6':
        ans = int_jmp_false(modes, numbers, inst_counter)
        if ans != 'bad':
            inst_counter = int(ans)
        else:
            inst_counter += 3
    elif instruction == '7':
        int_less_than(modes, numbers, inst_counter)
        inst_counter += 4
    elif instruction == '8':
        int_equals(modes, numbers, inst_counter)
        inst_counter += 4

print(numbers)

#p2 guess 8932273 too low