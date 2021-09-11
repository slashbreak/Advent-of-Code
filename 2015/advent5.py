import string
r1 = ["ab","cd","pq","xy"]
r2 = "aeiou"
r = "abcdefghijklmnopqrstuvwxyz"
r3 = [x+x for x in r]
print(r3)
lines = [l.strip() for l in open("input5.txt")]
nice = 0
#print(lines)
#print(len(lines))
def contains_vowels(str):
    count = 0
    m = [x for x in str if x in ["a","e","i","o","u"]]
    
    if len(m) > 2:
        return True
    return False

def contains_double_letter(str):
    chk = list(a+a for a in string.ascii_lowercase)
    m = [x for x in chk if x in str]
    if len(m) > 0:
        return True
        
    return False

def contains_bad_strings(str):
    chk = ["ab","cd","pq","xy"]
    m = [x for x in chk if x in str]
    if len(m) > 0:
        return False
    return True
def is_nice(i):
    if contains_vowels(i) and contains_double_letter(i) and contains_bad_strings(i):
        return True
    return False

def contains_repeated(str):
    is_nice = False
    for i in range(len(str)-1):
        
        start = str[i:i+2]
        #print("start " + start)
        for j in range(i+2, len(str)-1):
            next = str[j:j+2]
            
            if start == next:
                #print("next " + next)
                is_nice = True
    return is_nice
print("repeated: " + str(contains_repeated("aabqjhvhtzxzqqjkmpb")))

def contains_xyx(str):
    is_nice = False
    for i in range(len(str)-2):
        start = str[i]
        if start == str[i+2]:
            is_nice = True
    return is_nice
print("xyx " + str(contains_repeated("aabqjhvhtzxzqqjkmpb")))

def is_nice2(i):
    return contains_repeated(i) and contains_xyx(i)
nice = 0
nice2 = 0    
for i in lines:
    if is_nice(i):
        nice += 1
    if contains_repeated(i) and contains_xyx(i):
        nice2 += 1
print(contains_vowels("abai"))      
print("nice2 " + str(nice2))
print(contains_double_letter("ugknbfddgicrmopn"))
print("isnice2 " + str(contains_xyx("xxyxx")))