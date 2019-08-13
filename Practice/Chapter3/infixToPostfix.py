# 1. Scan infixexpr left to right
# 2. If current token is a letter or number, append it to output list
# 3. If left paran, push to opstack
# 4. If right paran, pop opstack until popping left paran
# 5. If operand, then first pop ALL operators of higher or = precedence, then push to opstack.
# 6. When done, check the opstack. If there are operators, pop and add to the output until opstack is empty

from Stack import Stack

def infixtopostfix(infixexpr): 
	prec = {}
	prec['('] = 1
	prec['+'] = 2
	prec['-'] = 2
	prec['*'] = 3
	prec['/'] = 3

	infixlist = infixexpr.split()
	opstack = Stack()
	output = []

	for token in infixlist: 
		if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token.isdigit():
			output.append(token)
		elif token == '(': 
			opstack.push('(')
		elif token == ')':
			toptoken = opstack.pop()
			while toptoken != '(':
				output.append(toptoken)
				toptoken = opstack.pop()
		else:  # if token is an operand (presumably)
			while (not opstack.isempty()) and (prec[opstack.peek()] >= prec[token]):
				output.append(opstack.pop())
			opstack.push(token)

	while not opstack.isempty(): 
		output.append(opstack.pop())
	return "".join(output)

if __name__ == '__main__':
	print(infixtopostfix('A * B + C * D'))
	print(infixtopostfix('( A + B ) * C - ( D - E ) * ( F + G )'))
