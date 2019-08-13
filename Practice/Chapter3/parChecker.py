from Stack import Stack
def parChecker(string): 
	index = 0
	balanced = True
	stack = Stack()
	while index < len(string) and balanced: 
		if string[index] == '(':
			stack.push('(')
		else: 
			if stack.isempty(): 
				balanced = False
			else: 
				stack.pop()
		index += 1

	if stack.isempty() and balanced: 
		return True
	else: 
		return False

if __name__ == '__main__':
	print(parChecker('(()'))