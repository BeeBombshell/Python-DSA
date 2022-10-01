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
         if data is not None:
            temp.left = TreeNode(data)
         else:
            temp.left = TreeNode(0)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         if data is not None:
            temp.right = TreeNode(data)
         else:
            temp.right = TreeNode(0)
         break
      else:
         que.append(temp.right)
def make_tree(elements):
   Tree = TreeNode(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree
class Solution(object):
   def postorderTraversal(self, root):
      if not root:
         return []
      res = []
      stack = [[root,0]]
      while stack:
         node = stack[-1]
         stack.pop()
         if node[1]== 0 :
            current = node[0]
            stack.append([current,1])
            if current.right:
               stack.append([current.right,0])
            if current.left:
               stack.append([current.left,0])
         else:
            if node[0].data != 0:
               res.append(node[0].data)
      return res

ob = Solution()
root = make_tree([-10,9,10,None,None,15,7])
print(ob.postorderTraversal(root))
