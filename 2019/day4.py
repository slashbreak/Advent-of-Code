#!/usr/bin/env python3

#AOC 2019 day4

min_pass = 137683
max_pass = 596253

def has_adjacent_pair(s):
    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return True
    return False

def is_ordered(number):
    temp = "".join(sorted(number))
    #print(temp, number)
    if temp == number:
        return True
    return False
'''    
good_count = 0
for i in range(min_pass, max_pass):
    if has_adjacent_pair(str(i)):
        if is_ordered(str(i)):
            good_count += 1
            #print('Good password: {}'.format(i))
print('N good passwords: {}'.format(good_count))
'''
def check_valid_adjacent(s):
    i = 1
    prev = s[0]
    count = 1
    good = False
    while i < len(s):
        
        current = s[i]
        #print(current, prev, count)
        if current == prev:
            count += 1
            good = False
            if count == 2:
                #print(current,prev,count)
                good = True
        else:
            if good:
                return True
            count = 1
        prev = current
        i+=1
    if good:
        return True
    return False

print(check_valid_adjacent('112233313433'))

print(check_valid_adjacent('111333'))
print(check_valid_adjacent('111334'))
print(check_valid_adjacent('123444'))

## just do ( str(i)*2 IN string AND str(i)*3 NOT IN string)


good_count = 0
for i in range(min_pass, max_pass):
    if check_valid_adjacent(str(i)):
        if is_ordered(str(i)):
            good_count += 1
            #print('Good password: {}'.format(i))
print('N good passwords: {}'.format(good_count))