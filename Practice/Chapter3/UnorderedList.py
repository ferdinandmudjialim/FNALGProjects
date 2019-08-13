from Node import Node

class UnorderedList: 
	def __init__(self): 
		self.head = None

	def isempty(self): 
		return self.head == None

	def add(self, item): 
		temp = Node(item)
		temp.next = self.head
		self.head = temp

	def size(self): 
		count = 0
		current = self.head
		while current != None:
			count += 1 
			current = current.next
		return count

	def search(self, item):
		current = self.head
		while current != None:
			if current.data == item: 
				return True
				break
			current = current.next
		else: 
			return False  

	def remove(self, item): 
		current = self.head
		previous = None
		if self.head.data == item:  # You can never have too many edge cases??
			self.head = current.next
		elif self.head == None: 
			return False
		else: 
			while current.next != None: 
				if current.data == item: 
					previous.next = current.next
					break
				else: 
					current = current.next
			else:  # Optional, but helpful for verbosity
				return False

	def append(self, item): 
		current = self.head
		previous = None
		while current != None:
			previous = current 
			current = current.next
		temp = Node(item)
		if current == self.head: 
			self.head = temp
		else: 
			previous.next = Node(item)

	def __str__(self):
		returnlist = ['UnorderedList contents:']
		current = self.head
		while current != None: 
			returnlist.append(str(current.data))  # Watch out! Data is int at first, not str
			current = current.next 
		return ' '.join(returnlist)

if __name__ == '__main__': 
	mylist = UnorderedList()
	print(mylist)
	mylist.add(31)
	mylist.add(77)
	print(mylist)
	print('Size', mylist.size())
	print(mylist.search(69))
	print(mylist.search(31))
	print(mylist.remove(69))
	print(mylist)
	mylist.remove(77)
	mylist.remove(31)
	mylist.append(69)
	print(mylist)
	mylist.append(420)
	print(mylist)