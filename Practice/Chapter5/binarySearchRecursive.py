# Practice: -2, don't forget base case!
def binarySearch(alist, item): 
	if len(alist) == 0:  # base case, exhausted search
		return False
	else: 
		midpoint = len(alist) // 2
		if alist[midpoint] == item: 
			return True
		else: 
			if item < alist[midpoint]: 
				return binarySearch(alist[:midpoint], item)
			else: 
				return binarySearch(alist[midpoint+1:], item)

if __name__ == '__main__':
	testlist = [0, 1, 2,8, 13, 17, 19, 32, 42]
	print(binarySearch(testlist, 3))
	print(binarySearch(testlist, 13))	
