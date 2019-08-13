from Stack import Stack  #parsetreeDAS.py
import operator

class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.
    """

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self, ):
        return self.key

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key,end=" ")
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key, end=" ")

    def preorder(self):
        print(self.key,end=" ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def printexp(self):
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printexp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printexp()
            print(')', end=' ')

    def postordereval(self):
        opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        res1 = None
        res2 = None
        if self.leftChild:
            res1 = self.leftChild.postordereval()  # // \label{peleft}
        if self.rightChild:
            res2 = self.rightChild.postordereval()  # // \label{peright}
        if res1 and res2:
            return opers[self.key](res1, res2)  # // \label{peeval}
        else:
            return self.key


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            currentTree = pStack.pop()
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def print_bracket_without_payload(p):
    if p:
        if (p.leftChild==None)  and (p.rightChild==None) :
            print("["+str(p.key)+"]",end="")
        else:
            print("["+str(p.key)+",",end=" ")
            print_bracket_without_payload(p.leftChild)
            print(",",end=" ")
            print_bracket_without_payload(p.rightChild)
            print("]", end=" ")

print()
print("the structure of the expression tree built")
#print("from the input '( ( 10 + 5 ) * 3 )' ")
#pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#print_bracket_without_payload(pt) #there is no payload here!!
print("from the input '((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'")
pt = buildParseTree("( ( ( ( 3 + 1 ) * 3 ) / \
     ( ( 9 - 5 ) + 2 ) ) - ( ( 3 * ( 7 - 4 ) ) + 6 ) )")
print_bracket_without_payload(pt) #there is no payload here!!
print()
print("evaluation of expression tree;")
print("...not to be confused with algorithm")
print("...used earlier for postfix evaluation")
print(pt.postordereval())
print()
print("inorder traversal of the expession tree;")
print("...which requires additional parenthesis")
print("...or operator precedence assumptions to")
print("...be properly interpreted!")
pt.inorder()
print()
print()
print("unambiuous fully parenthesized infix expression")
print("recovered from tree")
print(pt.printexp())
print()
print("preorder traversal producing unambiguous prefix expression:")
pt.preorder()
print()
print()
print("postorder traversal producing unambiguous postfix expression:")
pt.postorder()
print()



