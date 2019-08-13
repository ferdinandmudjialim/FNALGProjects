from Vertex import Vertex
class Graph:
    def __init__(self):
        self.vertList = {}  # 'A':(reference to Vertex A)
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]  # returns reference to Vertex obj
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,fromNode,toNode,cost=0):
        if fromNode not in self.vertList:  # if nodes don't exist yet, create them
            nv = self.addVertex(fromNode)  # why create an 'nv' variable?
        if toNode not in self.vertList:
            nv = self.addVertex(toNode)
        self.vertList[fromNode].addNeighbor(self.vertList[toNode], cost)  # adds to connectedTo dict in Vertex class

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
