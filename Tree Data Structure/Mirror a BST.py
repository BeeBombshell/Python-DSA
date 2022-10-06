class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data)
       inOrder(root.right)

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)

print inOrder(root)
# 4 2 1 5 3
print '\n'
mirror(root)
print inOrder(root)
# 5 3 1 4 2class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data)
       inOrder(root.right)

def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)

print inOrder(root)
# 4 2 1 5 3
print '\n'
mirror(root)
print inOrder(root)
# 5 3 1 4 2