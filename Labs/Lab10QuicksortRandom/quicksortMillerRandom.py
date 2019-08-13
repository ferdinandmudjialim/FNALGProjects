from random import *
import time

def quickSort(alist):
   return quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def quickSortRandom(alist):
   quickSortRandomHelper(alist,0,len(alist)-1)

def quickSortRandomHelper(alist,first,last):
   if first<last:

       splitpoint = partitionRandom(alist,first,last)
       quickSortRandomHelper(alist,first,splitpoint-1)
       quickSortRandomHelper(alist,splitpoint+1,last)


def partitionRandom(alist,first,last):
   randomindex = randint(first, last)
   pivotvalue = alist[randomindex]
   # switch the randomindex object with the first object to reuse code
   alist[randomindex] = alist[first]
   alist[first] = pivotvalue

   # pivotvalue = alist[first] # original code

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

randmax = 500
numbers = 10000
originallist = [randint(0,randmax) for x in range(numbers)]
alist = originallist.copy() # unsorted list

print("Random numbers from 0 to", randmax, "and list length of", numbers)
print("Miller quicksort unsorted list")
start = time.time()
quickSort(alist)
end = time.time()
print(end - start)

blist = alist.copy() # sorted list

print("Miller quicksort sorted list")
start = time.time()
quickSort(blist)
end = time.time()
print(end - start)

print("Random quicksort sorted list")
start = time.time()
quickSortRandom(blist)
end = time.time()
print(end - start)

alist = originallist.copy()

print("Random quicksort unsorted list")
start = time.time()
quickSortRandom(alist)
end = time.time()
print(end - start)