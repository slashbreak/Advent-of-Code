import threading
import queue

alphabet = 'abcdefghijklmnopqrstuvwxyz'
d1 = {}
d2 = {}
for c in alphabet:
    d1[c] = 0
    d2[c] = 0

d1['p'] = 0
d2['p'] = 1
ops = []

q = []
q.append(queue.Queue())
q.append(queue.Queue())
with open('input18.txt') as f:
    for l in f.readlines():
        ops.append(l.strip().split())

counter = 0
def run(_id, d):
    global counter
    if _id == 0:
        recFrom = 1
    else:
        recFrom = 0
    i = 0
    last = 0
    rec = 0
    while (i >= 0 and i < len(ops)):
        op = ops[i]
        if op[0] == 'snd':
            last = d[op[1]]
            q[_id].put(d[op[1]])
            i += 1
            if _id == 1:
                counter += 1
                
                
                #print(counter)
        elif op[0] == 'set':
            if op[2] not in d:
                d[op[1]] = int(op[2])
            else:
                d[op[1]] = d[op[2]]
            i += 1
        elif op[0] == 'add':
            if op[2] not in d:
                d[op[1]] += int(op[2])
            else:
                d[op[1]] += d[op[2]]
            i += 1
        elif op[0] == 'mul':
            if op[2] not in d:
                d[op[1]] *= int(op[2])
            else:
                d[op[1]] *= d[op[2]]
            i += 1
        elif op[0] == 'mod':
            if op[2] not in d:
                d[op[1]] %= int(op[2])
            else:
                d[op[1]] %= d[op[2]]
            i += 1
        elif op[0] == 'rcv':
            n = q[recFrom].get(True, 3)
            if n != None:
                d[op[1]] = n
            else:
                if _id == 1:
                    print(counter)
                    thread.exit()
                else:
                    thread.exit()
                #break
            i += 1
        elif op[0] == 'jgz':
            if op[1] in d:
                if d[op[1]] > 0:
                    if op[2] in d:
                        i += d[op[2]]
                    else:
                        i += int(op[2])
                else:
                    i += 1
            else:
                if int(op[1]) > 0:
                    if op[2] in d:
                        i += d[op[2]]
                    else:
                        i += int(op[2])
                else:
                    i += 1
                    
                    
    print(rec,last,i)


t1 = threading.Thread(target=run, args=(0, d1))
t2 = threading.Thread(target=run, args=(1, d2))
t1.start()
t2.start()
print('count', counter)

