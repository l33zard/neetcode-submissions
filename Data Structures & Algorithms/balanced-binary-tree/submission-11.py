# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0] 
            dL, dR = dfs(root.left), dfs(root.right) 
            if dL[0] and dR[0] and abs(dL[1] - dR[1]) <= 1:
                balanced = True
            else:
                balanced = False 
            return [balanced, 1 + max(dL[1], dR[1])]
        return dfs(root)[0]