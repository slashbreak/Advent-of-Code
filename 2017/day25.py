index = 0
#ABCDEF
#012345
curr = 0
d = {}
i = 0
while index < 12386363:
    if i not in d:
        d[i] = 0
    if curr == 0:
        if d[i] == 0:
            d[i] = 1
            i += 1
            curr = 1
        else:
            d[i] = 0
            i -= 1
            curr = 4
    elif curr == 1:
        if d[i] == 0:
            d[i] = 1
            i -= 1
            curr = 2
        else:
            d[i] = 0
            i += 1
            curr = 0
    elif curr == 2:
        if d[i] == 0:
            d[i] = 1
            i -= 1
            curr = 3
        else:
            d[i] = 0
            i += 1
            curr = 2
    elif curr == 3:
        if d[i] == 0:
            d[i] = 1
            i -= 1
            curr = 4
        else:
            d[i] = 0
            i -= 1
            curr = 5
    elif curr == 4:
        if d[i] == 0:
            d[i] = 1
            i -= 1
            curr = 0
        else:
            d[i] = 1
            i -= 1
            curr = 2
    elif curr == 5:
        if d[i] == 0:
            d[i] = 1
            i -= 1
            curr = 4
        else:
            d[i] = 1
            i += 1
            curr = 0
    index+=1
print(sum(i for i in d.values()))


