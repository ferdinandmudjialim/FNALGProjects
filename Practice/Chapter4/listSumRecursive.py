def listSum(list): 
	sum = 0
	for i in list: 
		sum += i
	return sum

def listSumRecursive(list):
	if len(list) == 1: 
		return list[0]
	else: 
		return list[0] + listSumRecursive(list[1:])

if __name__ == '__main__':
	print(listSum([1, 3, 5, 7, 9]))
	print(listSumRecursive([1, 3, 5, 7, 9]))