# Done
class Queue: 
	def __init__(self): 
		self.items = []

	def enqueue(self, item):  # adds item from "right"
		self.items.append(item)

	def dequeue(self):  # removes item from "left"
		return self.items.pop(0)

	def isempty(self): 
		return self.items == []

	def size(self): 
		return len(self.items)


