#look and say
#111221 becomes 312211
from itertools import groupby
def look_and_say(s):
    x = "".join(str(len(list(g))) + str(x) for x, g in groupby(s))
    return (x)
p = "1113122113"
for i in range(50):    
    p = look_and_say(p)
    print(look_and_say(p))
    a = raw_input()
print(len(p))