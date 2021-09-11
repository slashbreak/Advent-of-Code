with open('input9.txt') as f:
    for l in f.readlines():
        stream = l.strip()

depth, nGroups, nCanceled = 0, 0, 0
ignore , garbage = False, False

for c in stream:
    
    if ignore:
        ignore = False
        
    elif not garbage:
        if c == '{':
            depth += 1
            nGroups += depth
        if c == '}':
            depth -= 1
        if c == '<':
            garbage = True
            
    else:
        if c != '>' and c != '!':
            nCanceled += 1
        if c == '>':
            garbage = False    
        if c == '!':
            ignore = True
    
print(nGroups, nCanceled)
