# Practice: -1, don't forget base case!!
def mergeSort(alist): 
	print('Splitting ', alist)
	if len(alist) > 1: 
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0
		while i < len(lefthalf) and j < len(righthalf): 
			if lefthalf[i] < righthalf[j]:  # compares two smallest
				alist[k] = lefthalf[i]
				i += 1
			else: 
				alist[k] = righthalf[j]
				j += 1
			k += 1

		# exhaust extra items after comparing done
		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf): 
			alist[k] = righthalf[j]
			j += 1
			k += 1
	print('Merging ', alist)

if __name__ == '__main__':
	alist = [54,26,93,17,77,31,44,55,20]
	mergeSort(alist)
	print(alist)
