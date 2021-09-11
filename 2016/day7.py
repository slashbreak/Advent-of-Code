'''import re
count = 0

lines = open("input7.txt","r").readlines()
for text in lines:
    
    t = re.search(r"\[+[a-z]*([a-z])(?!\1)([a-z])\2\1[a-z]*\]+", text+"[")
    if t == None:
        s = re.search(r"[a-z]*([a-z])(?!\1)([a-z])\2\1[a-z]*", text+"[")
        if s != None: count += 1
#\[+[a-z]*(.+)(?!\1)(.+)\2\1[a-z]*\]+ #inside bracked match

#\]?[a-z]*([a-z]+)(?!\1)([a-z]+)\2\1[a-z]*\[+ #outside bracked
print count

'''

'''
import re
import os

import regex

def split_ip(ip):
    # Split based on []
    split = re.split(r'\[|\]', ip)
    # Divide into inside & outside []
    outside = split[::2]
    inside = split[1::2]

    return outside, inside

def support_tls(ip):
    outside, inside = split_ip(ip)

    # Don't match 4 in a row, but match abba
    abba_regex = r'(?!(\w)\1\1\1)(\w)(\w)\3\2'
    # Find any abba outside []
    abba_flag = False
    for o in outside:
        match = re.search(abba_regex, o)
        if match:
            abba_flag = True
            break

    # Check for no abba inside []
    inside_flag = False
    for i in inside:
        match = re.search(abba_regex, i)
        if match:
            inside_flag = True
            break

    if abba_flag and not inside_flag:
        return True
    return False

def support_ssl(ip):
    outside, inside = split_ip(ip)

    # Match three where the first and last are the same
    aba_regex = r'(\w)(\w)\1'

    # Find all possible aba matches
    aba_matches = []
    for o in outside:
        # Need to find overlapping matches
        overlapping_matches = regex.findall(aba_regex, o, overlapped=True)
        if overlapping_matches:
            aba_matches += overlapping_matches

    # Look for a bab in each inside segment
    for i in inside:
        # Check each aba match
        for aba in aba_matches:
            bab = aba[1] + aba[0] + aba[1]
            if bab in i:
                return True

    return False

def solve(data, ssl=True):
    if not ssl:
        return sum(support_tls(ip) for ip in data)
    else:
        return sum(support_ssl(ip) for ip in data)
print (solve(open("input7.txt", "r").readlines()))

'''
input_file_object = open("input7.txt")
input_as_string = input_file_object.read()
input_file_object.close()
 
def noDupes(some_list):
    temp = []
    for x in some_list:
        if x not in temp:
            temp.append(x)
    return temp
 
input_separated = input_as_string.split('\n')
 
for i in range(len(input_separated)):
    input_separated[i] = input_separated[i].replace('[',']')
    input_separated[i] = input_separated[i].split(']')
   
#input_separated[i][1] will be the hypernet sequence
 
hypernet_valid = []
hypernet_invalid = []
complete_valid = []
 
for i in range(len(input_separated)):
    #This for loop goes through the list of instructions
    for j in range(1,len(input_separated[i]), 2):
        #This for loop goes through the hypernet instructions
        for k in range((len(input_separated[i][j])-3)):
            #This for loop goes through the actual characters in the HNI
            if input_separated[i][j][k] == input_separated[i][j][k+3] and input_separated[i][j][k+1] == input_separated[i][j][k+2] and input_separated[i][j][k] != input_separated[i][j][k+1]:
                #If it finds an ABBA sequence
                hypernet_invalid.append(input_separated[i])
                break
        else:
            hypernet_valid.append(input_separated[i])
 
hypernet_valid = noDupes(hypernet_valid)
hypernet_invalid = noDupes(hypernet_invalid)
 
for i in range(len(hypernet_invalid)):
    if hypernet_invalid[i] in hypernet_valid:
        hypernet_valid.remove(hypernet_invalid[i])
       
for i in range(len(hypernet_valid)):
    #This for loop goes through options with a valid hypernet sequences
    for j in range(0, len(hypernet_valid[i]), 2):
        #This for loop goes through the non-hypernet sequences in each line
        for k in range((len(hypernet_valid[i][j])-3)):
            #This for loop goes through the actual characters
            if hypernet_valid[i][j][k] == hypernet_valid[i][j][k+3] and hypernet_valid[i][j][k+1] == hypernet_valid[i][j][k+2] and hypernet_valid[i][j][k] != hypernet_valid[i][j][k+1]:
                #ABBA Sequence found
                complete_valid.append(hypernet_valid[i])
                continue
 
 
complete_valid = noDupes(complete_valid)
print(len(complete_valid))
print("Searching for Super Secret Listening")
 
ssl_valid = []
counter = 0
 
for i in range(len(input_separated)):
    #
    for j in range(0,len(input_separated[i]),2):
        #only searches supernet
        for k in range((len(input_separated[i][j])-2)):
            if input_separated[i][j][k] == input_separated[i][j][k+2] and input_separated[i][j][k] != input_separated[i][j][k+1]:
                #ABA sequence found
                temp = []
                temp = input_separated[i][j][k:k+3]
                aba = ''.join(temp)
                temp = []
                temp = [aba[1],aba[0],aba[1]]
                bab = ''.join(temp)
                for m in range(1, len(input_separated[i]),2):
                    #
                    if bab in input_separated[i][m]:
                        ssl_valid.append(input_separated[i])
                        counter += 1
                        continue
 
ssl_valid = noDupes(ssl_valid)
 
print(len(ssl_valid))
