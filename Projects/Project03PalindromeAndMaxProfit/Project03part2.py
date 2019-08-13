import numpy as np

def maxprofit(weights, values, maxweight):
	rows = len(values) + 1
	cols = maxweight + 1
	a = np.zeros((rows, cols), dtype='int32')
	# a[1][0]=69 ----> a[row][column]=69
	for row in range(1, rows): 
		for col in range(1, cols): 
			bestValue1 = a[row-1][col]
			bestValue2 = 0
			newItemIndex = row-1
			if col-weights[newItemIndex] >= 0:  # check if adding another item would be allowed in weight limit
				# setting best value to value of newest item in subset + best value excluding the 
				# new item's weight in the previous subset
				bestValue2 = values[newItemIndex] + a[row-1][col-weights[newItemIndex]]
			a[row][col] = max([bestValue1, bestValue2])

	return a[rows-1][cols-1]  # returns bottom right hand corner of 2D array, the maximum
print('Max profit with weights [2,3,4,5,9], values [3,4,8,8,10], and weight limit 20')
print(maxprofit([2,3,4,5,9], [3,4,8,8,10], 20))
print('Max profit with weights [1,2,5,6,7], values [1,6,18,22,28], and weight limit 11')
print(maxprofit([1,2,5,6,7], [1,6,18,22,28], 11))

