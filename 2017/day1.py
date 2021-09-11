f = open('input1.txt','r').readline().rstrip('\n')

def part1(f):
    inLength = len(f)
    sum = 0
    for i, digit in enumerate(f):
        if i == inLength-1:
            if digit == f[0]:
                sum += int(digit)
        else:
            if digit == f[i+1]:
                sum += int(digit)
    return(sum)



    

def captcha(f, half=False):
    l = len(f) # expect even lengths
    step = 1
    if half: 
        step = l / 2
        
    sum = 0
    for i, digit in enumerate(f):
        if digit == f[(i+step) % l]:
            sum += int(digit)
    return sum

print(captcha(f))
print(captcha(f, True))
