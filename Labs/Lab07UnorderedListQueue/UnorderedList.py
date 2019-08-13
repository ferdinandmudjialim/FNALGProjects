# Ferdinand Mudjialim
# Lab 07
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next=self.head
        self.head = temp

    def pop(self):
        current = self.head
        previous = None

        while current.next != None:
            previous = current
            current = current.next

        if self.head.next == None:
            temp = self.head.data
            self.head = None
            return temp

        else:
            previous.next = None
            return current.data



    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current=current.next
        return count

    def __str__(self):
        returnString="The unordered list contents: "
        current = self.head
        while current != None:
            returnString = (returnString + " " + str(current.data))
            current = current.next
        return returnString

class Queue:

    def __init__(self):
        self.queuelist = UnorderedList()

    def isEmpty(self):
        return self.queuelist.size() == 0

    def enqueue(self, item):
        self.queuelist.add(item)

    def dequeue(self):
        return self.queuelist.pop()

    def size(self):
        return self.queuelist.size()

# the root(=main) starts here

q = Queue()
print(q.isEmpty())
print(q.size())
print(q.queuelist)

q.enqueue(136)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

q.enqueue(120)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

j=q.dequeue()
print("item removed is;",j)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

j=q.dequeue()
print("item removed is;",j)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

q.enqueue(101)
q.enqueue(135)
q.enqueue(105)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

j=q.dequeue()
print("item removed is;",j)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

j=q.dequeue()
print("item removed is;",j)
print(q.isEmpty())
print(q.size())
print(q.queuelist)


j=q.dequeue()
print("item removed is;",j)
print(q.isEmpty())
print(q.size())
print(q.queuelist)

# the root(=main) ends here
