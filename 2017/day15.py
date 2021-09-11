gen_a = 512
gen_b = 191
fact_a = 16807
fact_b = 48271
tomod = 2147483647
count = 0

def gen(n, reg):
    global fact_a
    global fact_b
    global tomod
    temp = n
    b= True
    if reg == 0:
        while b:
            temp = temp * fact_a
            temp %= tomod
            if temp%4 == 0:
                b = False
            #print(a)
    else:
        while b:
            temp = temp * fact_b
            temp %= tomod
            if temp%8 == 0:
                b = False
            #print(a)
    return temp
for i in range(5000000):
    
    gen_a = gen(gen_a, 0)
    
    gen_b = gen(gen_b, 1)
    
    if ((gen_a & 0xffff) == (gen_b & 0xffff)):
        count += 1
print(count)
