
import hashlib
key = "yzbqklnj"
count = 0
while True:
    h = hashlib.md5((key+str(count)).encode('utf-8')).hexdigest()
    
    if h[0:6] == "000000":
        print(count)
        break
    count+=1
