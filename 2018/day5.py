#! /usr/bin/env python3
with open('input5') as f:
    orig_polymer = f.read().strip()

def reduce_polymer(polymer):
    stack = []
    for i in polymer:
        if not stack:
            stack.append(i)
        elif abs(ord(stack[-1]) - ord(i)) == 32:
            stack.pop()
        else:
            stack.append(i)
    return ''.join(stack)
    
p1_polymer = reduce_polymer(orig_polymer)

d = {}
for c in 'abcdefghijklmnopqrstuvwxyz':
    trimmed = p1_polymer.replace(c,'').replace(c.upper(),'')
    d[c] = len(reduce_polymer(trimmed))
    
print ('Part 1: {}'.format(len(p1_polymer)))
print ('Part 2: {}'.format(min(d.values())))


'''
#print(polymer)
d = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    polymer = orig_polymer
    polymer = polymer.replace(i,'')
    polymer = polymer.replace(i.upper(),'')
    done = False
    pos = 0
    newstr = ""
    while not done:
        done = True
        while pos < len(polymer):
            if pos == len(polymer)-1:
                newstr += polymer[pos]
            elif abs( ord(polymer[pos]) - ord(polymer[pos+1]) ) == 32:
                pos += 1
                done = False
            else:
                newstr += polymer[pos]
            pos += 1
        pos = 0
        polymer = newstr
        newstr = ""
    d[i] = len(polymer)
    print(i,len(polymer))

print(min(d,key=d.get))
'''