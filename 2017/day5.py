values = []
with open('input5.txt') as f:
    for ln in f.readlines():
        values.append(int(ln.strip()))

count = 0
i = 0
x = len(values)    
while i >= 0  and i < x:
    count += 1
    temp = values[i]

    if temp > 2:
        values[i] -= 1
    else:
        values[i] += 1
    i += temp
    
print(count)

