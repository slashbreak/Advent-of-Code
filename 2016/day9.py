s = open("input9.txt","r").read()
s = s.strip('\n')
print(len(s))
i = 0
count = 0
output = ""
while True:
	if i >= len(s): break
	start = s[i]
	if start == "(":
		end_br = s.find(")",i) 
		op = s[i+1:end_br]
		
		(step, copies) = [int(x) for x in op.split('x')]	
		
		i = end_br +1
		output += (s[i:i+step]*copies)
		#print op, step, copies, s[i:i+step]
		#print output
		i += step
		 
	else:
		output += s[i]
		count += 1
		i += 1
#print count
#print "out : ", output, str(len(output))
print output
