if __name__ == '__main__':
	myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
	print(myTree)
	print('left subtree = ', myTree[1])
	print('root = ', myTree[0])
	print('right subtree = ', myTree[2])
	print('left subtree root = ', myTree[1][0])
	print('left - left subtree =', myTree[1][1])	
