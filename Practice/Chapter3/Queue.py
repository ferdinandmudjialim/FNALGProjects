# Done
class Queue: 
	def __init__(self): 
		self.items = []

	def addrear(self, item): 
		self.items.append(item)

	def removefront(self): 
		return self.items.pop(0)

	def isempty(self): 
		return self.items == []

	def size(self): 
		return len(self.items)

if __name__ == '__main__':
	q = Queue()
	print("Empty?", q.isempty())
	print("addrear 1", q.addrear(1))
	print("addrear 2", q.addrear(2))
	print("size", q.size())
	print("removefront", q.removefront())

