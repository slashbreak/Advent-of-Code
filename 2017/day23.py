comms = []
with open('input23.txt') as f:
    for l in f.readlines():
        comms.append(l.strip().split(' '))

regs = {}

for i in 'abcdefgh':
    regs[i] = 1
print(regs)
#regs['a'] = 1
index = 0
mulcount = 0
while True:
    if index < 0 or index >= len(comms):
        break
    print(index, comms[index],regs, raw_input())  
    op = comms[index]
    if op[0] == 'set':
        if op[2] in regs:
            regs[op[1]] = regs[op[2]]
        else:
            regs[op[1]] = int(op[2])
        index += 1
    elif op[0] == 'sub':
        if op[2] in regs:
            regs[op[1]] -= regs[op[2]]
        else:
            regs[op[1]] -= int(op[2])
        index += 1
    elif op[0] == 'mul':
        if op[2] in regs:
            regs[op[1]] *= regs[op[2]]
        else:
            regs[op[1]] *= int(op[2])
        index += 1
        mulcount += 1
    elif op[0] == 'jnz':
        if op[1] in regs:
            if regs[op[1]] != 0:
                if op[2] in regs:
                    index += regs[op[2]]
                else:
                    index += int(op[2])
            else:
                index += 1
        elif int(op[1]) != 0:
            if op[2] in regs:
                index += regs[op[2]]
            else:
                index += int(op[2])
            
        else:
            index += 1
    #print(index)
print('mul',mulcount, regs['h'],)