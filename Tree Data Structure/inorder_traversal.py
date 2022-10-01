class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right
def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         temp.left = TreeNode(data)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         temp.right = TreeNode(data)
         break
      else:
         que.append(temp.right)
def make_tree(elements):
   Tree = TreeNode(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree
class Solution(object):
   def inorderTraversal(self, root):
      res, stack = [], []
      current = root
      while True:
         while current:
            stack.append(current)
            current = current.left
         if len(stack) == 0:
            return res
         node = stack[-1]
         stack.pop(len(stack)-1)
         if node.data != None:
            res.append(node.data)
         current = node.right
      return res
ob1 = Solution()
root = make_tree([10,5,15,2,7,None,20])
print(ob1.inorderTraversal(root))
