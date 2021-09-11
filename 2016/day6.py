import collections

lines = open("input6.txt", "r").readlines()
lines[:] = [l.strip() for l in lines]

    
transposed = zip(*lines)
for l in transposed:
    s = "".join(l)
    print(collections.Counter(s).most_common())
