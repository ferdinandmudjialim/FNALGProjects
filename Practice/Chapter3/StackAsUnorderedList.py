from UnorderedList import UnorderedList

class StackAsUnorderedList: 
	def __init__(self): 
		self.stack = UnorderedList()  # Stack is client to UnorderedList, the supplier

	def isempty(self): 
		return self.stack.isempty()

	def push(self, item): 
		self.stack.add(item)

	def pop(self): 
		if self.stack.isempty(): 
			return 'Stack is empty'
		else: 
			temp = self.stack.head.data 
			self.stack.head = self.stack.head.next
			return temp

	def peek(self): 
		if self.stack.isempty(): 
			return 'Stack is empty'
		else:
			return self.stack.head.data

	def size(self): 
		return self.stack.size()

	def __str__(self): 
		return self.stack.__str__()

if __name__ == '__main__': 
	s = StackAsUnorderedList()
	print(s.isempty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print(s.size())
	print(s.isempty())
	s.push(8.4)
	print(s.pop())
	print(s.pop())
	print(s.size())