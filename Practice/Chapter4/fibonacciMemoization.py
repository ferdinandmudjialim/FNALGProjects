import time
# fibonacci(n) 0 1 2 3 4 ...
# fibsequence: 0 1 1 2 3 ...

cache = {}  # fibonacci cache
def fibonacci(n): 
	if n not in cache.keys(): 
		cache[n] = _fib(n)
	return cache[n]

def _fib(n): 
	if n <= 1: 
		return n  # return n b/c could be 0 or 1 
	else: 
		return fibonacci(n-1) + fibonacci(n-2)


# Versus fibonacci slow
def fibonaccislow(n): 
	if n <= 1: 
		return n
	else: 
		return fibonaccislow(n-1) + fibonaccislow(n-2)

def run(methodname): 
	nterms = 30
	list = []
	for i in range(nterms): 
		list.append(str(methodname(i)))
	print(','.join(list))

if __name__ == '__main__':
	print('Fib memoized:')
	start = time.time()
	run(fibonacci)
	end = time.time()
	print(end-start, 'seconds')
	print()
	print('Fib slow:')
	start = time.time()
	run(fibonaccislow)
	end = time.time()
	print(end-start, 'seconds')
