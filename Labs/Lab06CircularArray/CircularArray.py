class Deque:
    def __init__(self):
        self.items = [None] * 10
        self.size = 0
        self.front = 0

    def __str__(self):
        return str(self.items)

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.items[self.front]

    def resize(self, cap):
        old = self.items
        self.items = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0

    def peek(self):
        return self.items[self.front]

    def enqueue(self, item):
        if self.size == len(self.items):
            self.resize(2 * len(self.items))
        avail = (self.front + self.size) % len(self.items)
        self.items[avail] = item
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        answer = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.size -= 1
        return answer

    def addFront(self, item):
        if self.size == len(self.items): 
            self.resize(2 * len(self.items))
        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = item
        self.size += 1

    def removeRear(self):
        self.items[(self.front - (len(self.items) - self.size) - 1) % len(self.items)] = None
        self.size -= 1

    def removeFront(self):
        self.dequeue()

    def addRear(self, item):
        self.enqueue(item)


q = Deque()
print(q.isEmpty())
q.addFront(100)
print(q.size)
q.addFront(200)
q.addFront(500.58)
print(q.size)
print(q.peek())  # print the front item of the queue
q.addRear(500)
q.addRear(600)
q.addFront(3.14)
print(q.size)
print(q.peek())  # print the front item of the queue
q.removeFront()  # should be 5, but it's 6, fixed.
print(q.size)
print(q.peek())  # print the front item of the queue
q.addRear('True')
q.addRear('False')
print(q.size)
print(q.isEmpty())
q.addRear(8.4)
q.removeRear()  #
print(q.size)
print(q.peek())  # print the front item of the queue, but showing 'None'
q.addRear('C + +')
q.addRear('Python')
q.addRear('Java')
print(q.size)
q.addFront('Go')
q.addFront('C')
print(q.size)
print(q.dequeue())
q.removeFront()
q.removeFront()
print(q.size)

#  Extra Code Tests
# for i in range(10):
#     q.addFront(str(i) + "." + str(i))
#     print(q)
# for i in range(9):
#     print(q.removeFront())
# for i in range(10):
#     q.addRear(i)
#     print(q)
# print('------------------------------')
# print(q)
# q.removeRear()
# print(q)
# q.removeRear()
# print(q)
# q.addFront("$")  # tipping point
# print(q)
# for i in range(10):
#     q.addFront(i)
# print(q)
#
# q.removeRear()
# print(q)
# q.removeRear()
# print(q)
#
# for i in range(21):
#     q.addFront(i)
# print(q)
# q.addFront("break")  # tipping point
# print(q)
# q.removeRear()
# print(q)
# print(q)
# q.addFront("bruh")
# print(q)
# q.removeRear()
# print(q)
# q.removeRear()
# print(q)
# q.removeRear()
# print(q)
# q.removeRear()
# print(q)
