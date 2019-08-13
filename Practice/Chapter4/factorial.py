# non-recursive factorial
def factorial(n): 
	result = 1
	for i in range(1, n+1):
		result = result * i
	return result

def factorialRecursive(n):
	if n <= 1: 
		return 1
	else: 
		return n * factorialRecursive(n-1)

if __name__ == '__main__':
	print(factorial(5))
	print(factorialRecursive(5))
