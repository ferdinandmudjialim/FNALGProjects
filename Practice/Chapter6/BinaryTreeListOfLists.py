def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:  # if the left branch already has something
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:  # if the right branch already has something
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    tree = BinaryTree(1)
    print(tree)
    insertLeft(tree, 2)
    print(tree)
    insertLeft(tree, 3)
    print(tree)
    setRootVal(tree, 69)
    print(tree)    


# r = BinaryTree(3)
# insertLeft(r,4)
# insertLeft(r,5)
# insertRight(r,6)
# insertRight(r,7)
# l = getLeftChild(r)
# print(r)
# print(l)

# setRootVal(l,9)
# print(r)
# insertLeft(l,11)
# print(r)
# print(getRightChild(getRightChild(r)))
