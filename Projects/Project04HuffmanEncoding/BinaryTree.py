# Abbreviated BinaryTree class
# Parent reference has been added
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        self.parent = None  #DAS

    def insertLeft(self,newTree):  # FM, paramater newNode is now newTree
        if self.leftChild == None:
            self.leftChild = newTree  # no need to convert to BinaryTree
            self.leftChild.parent = self  #DAS
        else:
            t = newTree
            t.parent = self  #DAS
            t.leftChild = self.leftChild
            self.leftChild.parent = t  #DAS
            self.leftChild = t

    def insertRight(self,newTree):  # FM, paramater newNode is now newTree
        if self.rightChild == None:
            self.rightChild = newTree  # no need to convert to BinaryTree
            self.rightChild.parent = self  #DAS
        else:
            t = newTree
            t.parent = self  #DAS
            t.rightChild = self.rightChild
            self.rightChild.parent = t  #DAS
            self.rightChild = t

    def isLeaf(self): 
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getParent(self):  #DAS
        return self.parent

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key