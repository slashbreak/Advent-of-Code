#! /usr/bin/env python3
from itertools import islice
def addr(a, b):
    return reg[a] + reg[b]
def addi(a, b):
    return reg[a] + b
def mulr(a, b):
    return reg[a] * reg[b]
def muli(a, b):
    return reg[a] * b
def banr(a, b):
    return reg[a] & reg[b]
def bani(a, b):
    return reg[a] & b
def borr(a, b):
    return reg[a] | reg[b]
def bori(a, b):
    return reg[a] | b
def setr(a, b):
    return reg[a]
def seti(a, b):
    return a
def gtir(a, b):
    if a > reg[b]: return 1
    else: return 0
def gtri(a, b):
    if reg[a] > b: return 1
    else: return 0
def gtrr(a, b):
    if reg[a] > reg[b]: return 1
    else: return 0
def eqir(a, b):
    if a == reg[b]: return 1
    else: return 0
def eqri(a, b):
    if reg[a] == b: return 1
    else: return 0
def eqrr(a, b):
    if reg[a] == reg[b]: return 1
    else: return 0

opcode_possible = []
for i in range(16):
    op = []
    for fun in (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr):
        op.append(fun.__name__)
    opcode_possible.append(op)
    
befores = []
init_registers = []
afters = []
lines = []
with open('input16') as f:
    while True:
        next_n = list(islice(f,4))
        #print(next_n)
        #input()
        if len(next_n[0]) < 2:
            break
        if not next_n:
            break
        befores.append(list(map(int,next_n[0].strip()[9:][:-1].split(', '))))
        init_registers.append(list(map(int,next_n[1].strip().split())))
        afters.append(list(map(int,next_n[2].strip()[9:][:-1].split(', '))))
        #print(befores)
    for l in f.readlines():
        lines.append(list(map(int, l.strip().split())))
total = 0
for i in range(len(befores)):
    #print(befores[i], init_registers[i], afters[i])
    count = 0
    for fun in (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr):
        start = befores[i]
        end = afters[i]
        reg = {}
        for x in range(4):
            reg[x] = start[x]
        opcode,a,b,c = init_registers[i]
        reg[c] = fun(int(a),int(b))
        to_test = [reg[0], reg[1], reg[2], reg[3]]
        if( to_test != end ):
            if fun.__name__ in opcode_possible[opcode]:
                
                opcode_possible[opcode].remove(fun.__name__)
        else:
            count += 1
            #print(fun.__name__,reg[0], reg[1], reg[2], reg[3])
    if count >= 3: 
        total += 1
    #for j, op in enumerate(opcode_possible):
    #    print(j, op)
    #input()
print(total)
for x in range(16):
    for i in range(16):
        if len(opcode_possible[i]) == 1:
            for j in range(16):
                if i != j:
                    if opcode_possible[i][0] in opcode_possible[j]:
                        opcode_possible[j].remove(opcode_possible[i][0])
for j, op in enumerate(opcode_possible):
        print(j, op)
#print(lines)

reg = {}
reg[0] = 0
reg[1] = 0
reg[2] = 0
reg[3] = 0
for opcode, a, b, c in lines:
    x = opcode_possible[opcode][0]
    #print(a)
    m = locals()[x](a,b)
    #func = getattr(m, 'function_name')
    reg[c] = m
print(reg[0])