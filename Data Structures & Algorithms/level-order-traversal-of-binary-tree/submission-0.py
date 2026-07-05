# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque([root])
       
        # val =[]
        res =[]

        if root is None:
            return []

        while q:
            val = []

            for i in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res

        # while q:
        #     curr = q.popleft()
        #     val.append(curr.val)

        #     if curr.left:
        #         q.append(curr.left)
        #         # val.append(curr.left.val)

        #     if curr.right:
        #         q.append(curr.right)
        #         # val.append(curr.right.val) 

        # return val

        


        