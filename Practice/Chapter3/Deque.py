# Done
class Deque: 
	def __init__(self): 
		self.items = []

	def addrear(self, item): 
		self.items.append(item)

	def removefront(self): 
		return self.items.pop(0)

	def addfront(self, item): 
		self.items.insert(0, item)  # be careful of insert() ordering!!

	def removerear(self): 
		return self.items.pop()

	def isempty(self): 
		return self.items == []

	def size(self): 
		return len(self.items)

if __name__ == '__main__':
	d = Deque()
	print("Empty?", d.isempty())
	print("addrear 1", d.addrear(1))
	print("addrear 2", d.addrear(2))
	print("addrear 3", d.addrear(3))
	print("size", d.size())
	print("removefront", d.removefront())
	print("removerear", d.removerear())
	print("addfront", d.addfront(69))
	print(d.items)
