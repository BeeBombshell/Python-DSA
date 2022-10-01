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
   def maxPathSum(self, root):
      self.ans = -float('inf')
      self.solve(root)
      return self.ans
   def solve(self,node):
      if not node or node.data == 0:
         return 0
      left = max(0,self.solve(node.left))
      right = max(0,self.solve(node.right))
      self.ans = max(self.ans,left+right+node.data)
      return node.data + max(left,right)
ob = Solution()
root = make_tree([-10,9,10,None,None,15,7])
print(ob.maxPathSum(root))
