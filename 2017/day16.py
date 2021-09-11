#abcdefghijklmnop
#kgdchlfniambejop
#abdkcgfepimjnlho
#0123456789abcdef
with open('input16.txt') as f:
    for l in f.readlines():
        moves = l.strip().split(',')
letters = 'abcdefghijklmnop'
programs = list(letters)
print(programs)
def spin(p, i):
    return p[-1*i:] + p[:-1*i]
    
def exchange(p, a, b):
    p = list(p)
    p[a], p[b] = p[b], p[a]
    return "".join(p)
    
def partner(p, a, b):
    p = list(p)
    tempA = p.index(a)
    tempB = p.index(b)
    temp = p[tempA]
    p[tempA] = p[tempB]
    p[tempB] = temp
    return "".join(p)
        
def dance(prog, mo):
    
    for i in range(1000000000%42):
        for m in mo:
            
            if m[0] == 's':
                prog = spin(prog, int(m[1:]))
            elif m[0] == 'x':
                a, b = m[1:].split('/')
                prog = exchange(prog, int(a), int(b))
            elif m[0] == 'p':
                a, b = m[1:].split('/')
                prog = partner(prog, a, b)
        if prog == letters:
            print(i)
    return prog
#print(spin('abcde', 2))
print(exchange('abcde', 3, 1))
print(spin('abcde', 2))
print(partner('abcde', 'a', 'c'))
print(dance(programs,moves))
