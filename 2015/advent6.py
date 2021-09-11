lines = [x.strip().split() for x in open("input6.txt")]
grid = [[0 for x in range(1000)] for x in range(1000)]
cp = 0
for i in lines:
    print(cp)
    cp+=1
    inst, x0, y0, x1, y1 = i
    x0 = int(x0)
    x1 = int(x1)
    y0 = int(y0)
    y1 = int(y1)
    if inst == 'on':
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] += 1
    if inst == 'off':
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] -= 1
                if grid[i][j] < 0: grid[i][j] = 0
    if inst == 'toggle':
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                grid[i][j] += 2
print(sum(map(sum,grid)))
            