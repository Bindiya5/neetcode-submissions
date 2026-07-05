# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    # def dfs(self, root: Optional[TreeNode]) -> list:

    #     if root is None:
    #         return [None]   
    #     leftdfs = self.dfs(root.left)
    #     rightdfs = self.dfs(root.right)
    #     return [root.val] + leftdfs + rightdfs

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     return self.dfs(p) == self.dfs(q)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        if not p and not q:
            return True 

        if not p or not q or p.val != q.val:
            return False 

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        
    



        