import itertools
from collections import defaultdict

lines = open("input4.txt", "r").readlines()
count = 0
keys = 'abcdefghijklmnopqrstuvwxyz'
for line in lines:
    checksum = line[-7:-2]
    code = line[-11:-8]
    text = line[:-11]
    dic = defaultdict(lambda: 0)
    for ch in text:
        if ch != '-':
            dic[ch] += 1
    a = "".join([v[0] for v in sorted(dic.items(), key=lambda(k,v): (-v,k))])
    if a[0:5] == checksum:
        count += int(code)
        print code, a[0:5], checksum,
        result = ""
        for l in text:
            if l == '-': result += " "
            else:
                i = (keys.index(l) + int(code))%26
                result += keys[i]
        print result
    #print text, code, checksum
print count
#dic = {'a':4,'b':4,'c':5,'d':1}
