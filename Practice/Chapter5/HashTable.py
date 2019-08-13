# Practice: -4, put and get methods
class HashTable: 
	def __init__(self): 
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data): 
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:  # if there's nothing yet put key and data
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else: 
			if self.slots[hashvalue] == key: 
				self.data[hashvalue] = data  # replace if key is equal
			else: 
				nextslot = self.rehash(hashvalue, len(self.slots))  # need to rehash
				while self.slots[nextslot] != None and self.slots[nextslot] != key: 
					nextslot = self.rehash(nextslot, len(self.slots))

				if self.slots[nextslot] == None: 
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else: 
					self.data[nextslot] = data  # replace if key is equal

	def hashfunction(self, key, size): 
		return key % size

	def rehash(self, oldhash, size): 
		return (oldhash + 1) % size

	def get(self, key): 
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and \
				not found and not stop:
			if self.slots[position] == key: 
				found = True
				data = self.data[position]
			else: 
				position = self.rehash(position, len(self.slots))
				if position == startslot: 
					stop = True
		return data

	def __getitem__(self, key):  # overloading of [] to get/set items with keys, not indexes
		return self.get(key)

	def __setitem__(self, key, data): 
		self.put(key, data)

if __name__ == '__main__':
	H = HashTable()
	H[54] = 'cat'
	H[26] = 'dog'
	H[93] = 'lion'

	print(H.slots)
	print(H.data)

	print(H[54])
	print(H[99])  # not in the table