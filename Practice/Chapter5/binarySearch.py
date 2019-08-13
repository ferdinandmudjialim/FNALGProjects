# Practice: -2, review the while case
def binarySearch(alist, item): 
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:  # don't forget the not found!
		midpoint = (first + last) // 2  # don't do len(alist)!!
		if alist[midpoint] == item: 
			found = True
		else: 
			if item < alist[midpoint]: 
				last = midpoint - 1
			else: 
				first = midpoint + 1
	return found

if __name__ == '__main__':
	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(binarySearch(testlist, 3))
	print(binarySearch(testlist, 13))