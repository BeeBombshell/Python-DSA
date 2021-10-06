#class  made for node of tree
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
#class made for tree
class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    #to add a new node in tree
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
            
    # to add elemnts in tree
    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)
    #to find an element if present in root node in tree
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None
    # to find any element in tree
    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    #to print the tree
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
print(tree.find(10))
tree.deleteTree()
tree.printTree()