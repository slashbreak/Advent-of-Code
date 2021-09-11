#!/usr/bin/env python3
reg = [1,0,0,0,0,0]
reg = {}
reg[0] = 1
reg[1] = 0
reg[2] = 0
reg[3] = 0
reg[4] = 0
reg[5] = 0
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
    
ip_reg = -1
program = []
with open('input19') as f:
    ip_reg = int(f.readline().strip().split()[1])
    for l in f.readlines():
        inst, a,b,c = l.strip().split()
        a,b,c = map(int,(a,b,c))
        program.append([inst,a,b,c])
#for i in program:
#    print(i)
print('ip',ip_reg)
print(reg)

ip = reg[ip_reg]
print(ip)
while ip >= 0 and ip < len(program):
    #print(ip, program[ip], (reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])),
    a = program[ip]
    reg[a[3]] = eval(a[0])(a[1],a[2])

    reg[ip_reg] += 1
    ip = reg[ip_reg]
    #print(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
    #raw_input()
print(reg)

