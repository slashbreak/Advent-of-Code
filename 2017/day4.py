count = 0
with open('input4.txt') as f:
    for ln in f.readlines():
        chunks = ln.strip().split(' ')
        valid = True
        for i in range(len(chunks)-1):
            for j in chunks[i+1:]:
                if j == chunks[i]:
                    valid = False
                    break
        if valid:
            count +=1
        valid = True

print(count)


#part 2

count = 0

with open('input4.txt') as f:
    for ln in f.readlines():
        chunks = ln.strip().split(' ')
        valid = True
        for i in range(len(chunks)-1):
            for j in chunks[i+1:]:
                if j == chunks[i] or sorted(j) == sorted(chunks[i]):
                    valid = False
                    break
            if not valid:
                break
        count += int(valid)

print(count)

