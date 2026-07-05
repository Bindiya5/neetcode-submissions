# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxCount):

            if not node:
                return 0

            res = 1 if node.val >= maxCount else 0

            maxCount = max(maxCount, node.val)
            res += dfs(node.left, maxCount)
            res += dfs(node.right, maxCount)

            return res

        return dfs(root, root.val)

            

        