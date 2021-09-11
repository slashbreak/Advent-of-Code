# spiral generator with 2d dictionary

key = 325489

space = {0:{0:1}}

#space[0][0] = 1
count = 0
def spiral():
    global count
    direction = [ [1, 0],[0, 1],[-1, 0],[0, -1] ] # order: R U L D
    all_dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] # 8 dir
    i = dx = dy = 0
    edge_length = 0 # every two iterations, increase length by 1
    
    while True: # build an edge at a time
        if i % 2 == 0: # increase edge length
            edge_length += 1
        for j in range(edge_length):
            # add values
            dx += direction[i%4][0] # using outer loop as counter for direction
            dy += direction[i%4][1]
            
            if dx not in space:
                space[dx] = {}
            if dy not in space[dx]:
                space[dx][dy] = 0
            
            
            total = 0
            for d in all_dir:
                a = dx + d[0]
                b = dy + d[1]
                if a in space and b in space[a]:
                    total += space[dx+d[0]][dy+d[1]]
                    count += 1
            space[dx][dy] = total

            if space[dx][dy] > key:
                print(space[dx][dy])
                return
        i += 1

spiral()
print(count)
