b = 84
c = b
b *= 100
b += 100000
c = b + 17000
h = 1
while (b-c) != 0:
    f = 1
    for d in range(2, b):
        if b%d == 0 : 
            f = 0                
            break    
    if f == 0: 
        h+=1

    b += 17
print(h)