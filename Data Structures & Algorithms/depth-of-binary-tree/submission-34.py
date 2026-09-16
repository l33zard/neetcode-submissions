# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def dfs(root):
            if not root:
                return 0 
            dL, dR = self.maxDepth(root.left), self.maxDepth(root.right) 
            depth = 1 + max(dL, dR)
            self.res = depth
            return depth
        dfs(root) 
        return self.res