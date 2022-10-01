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
   def preorderTraversal(self, root):
      res = []
      st = []
      node = root
      while node or st:
         while node:
            if node.data != None:
               res.append(node.data)
            st.append(node)
            node = node.left
         temp = st[-1]
         st.pop()
         if temp.right:
            node = temp.right
   return res
ob1 = Solution()
head = make_tree([3,9,20,None,None,15,7])
print(ob1.preorderTraversal(head))
