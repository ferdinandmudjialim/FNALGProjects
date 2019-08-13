# Done
from Stack import Stack

def baseConverter(decimal, base): 
	num = decimal
	digits = '0123456789ABCDEF'
	s = Stack()
	resultlist = []

	while num > 0: 
		s.push(digits[num % base])	
		num = num // base

	while not s.isempty(): 
		resultlist.append(s.pop())

	return "".join(resultlist)

print(baseConverter(10, 16))