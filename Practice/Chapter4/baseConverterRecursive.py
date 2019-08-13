def toStr(n, base): 
	digits = '0123456789ABCDEF'
	if n < base: 
		return digits[n]
	else:
		return toStr(n // base, base) + digits[n % base]  # Two parameters in toStr and modulo operator

if __name__ == '__main__':
	print(toStr(25, 2))
	print(toStr(25, 16))
	print(toStr(1453, 16))