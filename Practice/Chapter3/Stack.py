# Done
class Stack:
	def __init__(self): 
		self.items = []

	def push(self, item): 
		self.items.append(item)

	def pop(self): 
		return self.items.pop()

	def peek(self):
		return self.items[self.size() - 1]  # CAREFUL! It's the Stack's size, not the list's.

	def isempty(self): 
		return self.items == []

	def size(self): 
		return len(self.items)

if __name__ == '__main__':
	s = Stack()
	print("Empty?", s.isempty())
	print("push 1", s.push(1))
	print("push 2", s.push(2))
	print("size", s.size())
	print("pop", s.pop())
	print("pop", s.pop())
