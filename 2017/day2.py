
rows = []

with open('input2.txt') as f:
    for l in f:
        row = [int(a) for a in l.strip().split("\t") ]
        rows.append(sorted(row))

checksum = 0
for r in rows:
    diff = r[-1] - r[0]
    checksum += diff
print(checksum)

checksum2 = 0
for r in rows:
    for i, num in enumerate(r):
        for j in range(len(r)):
            if (1.0 * num) % r[j] == 0 and i != j:
                checksum2 += (1.0 * num) / r[j]
                print(str(num) + " and " + str(r[j]) )
                
print (checksum2)
