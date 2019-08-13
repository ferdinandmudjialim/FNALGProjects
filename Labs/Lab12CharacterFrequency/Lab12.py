# Ferdinand Mudjialim
# Lab 12
with open('Project04Input.txt') as fp: 
	string = fp.read()

print(string)
stringlist = list(string)
print(stringlist)
stringdict = {}
for char in stringlist: 
	if char not in stringdict.keys(): 
		stringdict[char] = 1
	else: 
		stringdict[char] += 1
print(stringdict)
