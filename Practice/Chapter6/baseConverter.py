def baseConverter(num, base): 
	digits = '0123456789ABCDEF'
	if num < base: 
		return digits[num]
	else: 
		return baseConverter(num//base, base) + digits[num%base]

if __name__ == '__main__':
	print(baseConverter(769, 8))