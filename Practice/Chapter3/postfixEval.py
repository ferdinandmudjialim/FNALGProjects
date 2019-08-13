'''
    Create an empty stack called operandstack.
    Convert the string to a list by using the string method split.
    Scan the token list from left to right.
        If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
        If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the operandStack.
    When the input expression has been completely processed, the result is on the stack. Pop the operandStack and return the value.
'''
from Stack import Stack

def postfixEval(postfixexpr):
	operandstack = Stack()
	tokenlist = postfixexpr.split()

	for token in tokenlist: 
		if token.isdigit(): 
			operandstack.push(int(token))
		else:  # if token is an operator (presumably)
			int2 = operandstack.pop()
			int1 = operandstack.pop()
			result = doMath(int1, int2, token)
			operandstack.push(result)
	return operandstack.pop()

def doMath(int1, int2, token): 
	if token == '+':
		return int1 + int2
	elif token == '-':
		return int1 - int2
	elif token == '*':
		return int1 * int2
	elif token == '/':
		return int1 / int2

if __name__ == '__main__':
	print(postfixEval('3 1 2 + *'))