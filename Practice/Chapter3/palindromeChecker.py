from Deque import Deque
def palindromeChecker(string): 
	d = Deque()
	if len(string) == 1:  # Optional edge case
		return True
	for char in string: 
		d.addrear(char)
	while d.size() > 1: 
		if d.removerear() != d.removefront(): 
			return False
		else: 
			return True

if __name__ == '__main__': 
	print(palindromeChecker('kappa'))
	print(palindromeChecker('kapak'))
	print(palindromeChecker('kappak'))
	print(palindromeChecker('k'))