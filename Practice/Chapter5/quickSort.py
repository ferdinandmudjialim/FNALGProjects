# Practice: -4, Partition: while not done, while, and RETURN, don't forget (if first<last)
def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last): 
	if first < last: # trust that this is condition

		splitpoint = partition(alist, first, last) # moves everything relative to splitpoint

		quickSortHelper(alist, first, splitpoint-1) # sorts left side
		quickSortHelper(alist, splitpoint+1, last) # sorts right side

def partition(alist, first, last): 
	pivotvalue = alist[first]

	leftmark = first+1
	rightmark = last

	done = False
	while not done: 

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark += 1

		while rightmark >= leftmark and alist[rightmark] >= pivotvalue: 
			rightmark -= 1

		if rightmark < leftmark:  # cross-over of marks
			done = True
		else: 
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark

if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	quickSort(alist)
	print(alist)
