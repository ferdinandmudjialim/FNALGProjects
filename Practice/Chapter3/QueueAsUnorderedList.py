'''
To make Queue (FIFO) in LinkedList enqueue/dequeue efficient, 
have a head (left) and tail (right) reference. 
Enqueue at the rear on the right and dequeue on the other side.
Why not the other way around? IF you dq on the right, then you must 
have a previous reference to set previous.next = None. There is no such
problem when dq'ing on the left and enq'ing on the right. 
'''
from UnorderedList import UnorderedList
from Node import Node

class QueueAsUnorderedList: 
	def __init__(self): 
		self.queue = UnorderedList()
		self.tail = None

	def enqueue(self, item): 
		if self.queue.head == None: 
			self.queue.head = Node(item)
		elif self.queue.head.next == None: 
			temp = Node(item)
			self.queue.head.next = temp
			self.tail = temp
		else: 
			temp = Node(item)
			self.tail.next = temp
			self.tail = temp

	def dequeue(self): 
		self.queue.head = self.queue.head.next

	def isempty(self): 
		return self.queue.isempty()

	def size(self): 
		return self.queue.size()

	def __str__(self):
		return self.queue.__str__()
			
if __name__ == '__main__':
	q = QueueAsUnorderedList()
	print(q.isempty())
	q.enqueue(1)
	print(q)
	q.enqueue(2)
	print(q)
	print(q.size())
	print(q.isempty())
	q.dequeue()
	print(q)