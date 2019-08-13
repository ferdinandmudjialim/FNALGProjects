from Node import Node

class OrderedList: 
	def __init__(self): 
		self.head = None

	def isempty(self): 
		return self.head == None

	def add(self, item): 
		temp = Node(item)
		previous = None
		current = self.head
		while current != None:
			if current.data > item: 
				break 
			previous = current  # Inch worming - order is important!!
			current = current.next
		if current == self.head: 
			temp.next = self.head
			self.head = temp
		else: 
			temp.next = current
			previous.next = temp

	def size(self):
		current = self.head
		count = 0 
		while current != None: 
			count += 1
			current = current.next
		return count

	def search(self, item): 
		current = self.head 
		while current != None: 
			if current.data > item: 
				return False
			elif current.data == item: 
				return True
			current = current.next
		else: 
			return False

	def remove(self, item): 
		previous = None
		current = self.head
		while current != None: 
			if current.data == item: 
				break
			else: 
				previous = current
				current = current.next

		if current == self.head: 
			self.head = current.next
		else: 
			previous.next = current.next

	def __str__(self):
		returnlist = ['OrderedList contents:']
		current = self.head
		while current != None: 
			returnlist.append(str(current.data))  # Watch out! Make sure to convert to string!!!
			current = current.next
		return ' '.join(returnlist)

if __name__ == '__main__': 
	mylist = OrderedList()
	print(mylist)
	mylist.add(31)
	mylist.add(77)
	mylist.add(17)
	print(mylist)
	mylist.add(93)
	mylist.add(26)
	mylist.add(54)
	print(mylist)
	mylist.remove(54)
	print(mylist)
	print(mylist.search(54))
	print(mylist.search(77))
	
