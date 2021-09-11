import md5
import sys
#import bytearray

input_id = "ffykfhsq"
#input_id = "abc"
result = ['x','x','x','x','x','x','x','x']
i = 1
'''
result = ""
while True:
    m = md5.new(input_id + str(i))
    if m.hexdigest()[0:5] == '00000':
        result += m.hexdigest()[5]
        print result, i
        raw_input()
    i+=1
    if len(result) == 8:
        print result'''
        
while True:
    m = md5.new(input_id + str(i))
    mhex = m.hexdigest()
    #print mhex
    if mhex[0:5] == '00000':
        mpos = mhex[5]
        mval = mhex[6]
        if mpos in "01234567":
            if result[int(mpos)] == 'x':
                result[int(mpos)] = mval
        text = "".join(result)
        sys.stdout.write('\r'+str(text))
        sys.stdout.flush()
    i+=1
    
