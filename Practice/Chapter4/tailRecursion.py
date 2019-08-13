def countDown(n): 
	if (n == 0): 
		return 0
	print(str(n) + '...')
	# waitASecond()
	countDown(n - 1)

print(countDown(6))

# tail recursion can be replaced with iteration

def countDownIterate(n): 
	while (n > 0): 
		print(str(n) + '...')
		# waitASecond()
		n -= 1

print(countDownIterate(6))