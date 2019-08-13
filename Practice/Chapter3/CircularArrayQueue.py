class CircularArrayQueue:
	def __init__(self): 
		self.items = [None] * 10
		self.size = 0
		self.front = 0

	def resize(self, cap): 
		old = self.items
		self.items = [None] * cap
		walk = self.front
		for i in range(self.size): 
			self.items[i] = old[walk]
			walk = (walk + 1) % len(old)
		self.front = 0  # Don't forget to set the front as 0

	def enqueue(self, item): 
		if self.size == len(self.items): 
			self.resize(2 * len(self.items))  # Make sure to resize on "self" and not "self.items"
		nextindex = (self.front + self.size) % len(self.items)  # Where is front? Does it change pos? 
		self.items[nextindex] = item
		self.size += 1  # Don't forget to increment size

	def dequeue(self): 
		if self.size == 0: 
			raise Exception('Queue is empty')
		answer = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front + 1) % len(self.items)
		self.size -= 1  # Don't forget to decrement size
		return answer  # Don't forget to return something for dequeue

if __name__ == '__main__': 
	c = CircularArrayQueue()
	for i in range(10): 
		c.enqueue(i)
	print(c.items)
	print('Front:', c.front)
	print('Dequeuing...', c.dequeue())
	print(c.items)
	print('Front:', c.front)