# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def dfs(root):
            if not root:
                return 0 
            dL, dR = dfs(root.left), dfs(root.right) 
            self.res = max(self.res, dL + dR) 
            return 1 + max(dL, dR)
        dfs(root) 
        return self.res