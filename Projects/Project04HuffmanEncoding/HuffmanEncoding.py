from PriorityQueue import PriorityQueue
from BinaryTree import BinaryTree

def frequency(string):  # builds dictionary of frequency of each char
	mylist = list(string)
	mydict = {}
	for key in mylist: 
		if key not in mydict.keys():
			mydict[key] = 1
		else: 
			mydict[key] += 1
	return mydict

def huffman(str): 
	freqdict = frequency(str)
	pq = PriorityQueue()

	for char in freqdict:  # NOT for char in STRING!!
		t = BinaryTree(char)
		key = freqdict[char]
		pq.add((key, t))

	while pq.getSize() > 1:
		u = pq.delMin()
		v = pq.delMin()
		t = BinaryTree(u[0]+v[0])  
		t.insertLeft(u[1])  # inserts left subtree T1
		t.insertRight(v[1]) # inserts right subtree T2
		pq.add((u[0]+v[0], t))  # inserts T into PQ with key f1 + f2 (from u and v tuples)

	result = pq.delMin()  # tuple of (freq, T)
	return result[1]  # returns the final tree, T

huffmandict = {}  # huffman encoding dictionary / table
def buildDict(node):
	if node.isLeaf():
		originalnode = node
		encoding = ''
		while node.getParent():
			if node.getParent().getRightChild() == node:
				encoding += '1'
			elif node.getParent().getLeftChild() == node:
				encoding += '0'
			node = node.getParent()
		huffmandict[originalnode.getRootVal()] = encoding[::-1]  # this reverses the encoding (like a stack)

def visitAllSubnodes(node):  # visits all subnodes
	if node != None: 
		if node.getLeftChild():
			visitAllSubnodes(node.getLeftChild())
		buildDict(node)  # adds an entry to the huffman encoding dictionary for each leaf (see above)
		if node.getRightChild():
			visitAllSubnodes(node.getRightChild())


def main(): 
	file = 'Project04Input.txt'
	with open(file) as fp: 
		string = fp.readline()
	print('Original String \n', string, '\n')
	print('Frequency Table \n', frequency(string), '\n')
	huffmantree = huffman(string)

	visitAllSubnodes(huffmantree)  # Uses buildDict to build an encoding dictionary
	print('Huffman Encoding Table \n', huffmandict, '\n')

	encodedStringList = []
	for char in string: 
		encodedStringList.append(huffmandict[char])
	encodedString = '|'.join(encodedStringList)
	print('Encoded String with Delimiters \n', encodedString, '\n')


if __name__ == '__main__':
	main()

