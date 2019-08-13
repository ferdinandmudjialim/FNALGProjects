from PriorityQueue import PriorityQueue
from Graph import Graph
from Vertex import Vertex

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])  # builds heap from list
    while not pq.isEmpty():
        currentVert = pq.delMin()  # start with the lowest distance item first
        for nextVert in currentVert.getConnections():  # for each connected node...
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)  # is this like bubbling up the priority? 