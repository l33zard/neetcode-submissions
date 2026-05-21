# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        left = self.height(root.left)
        right = self.height(root.right)
        heightD = abs(left - right)
        return heightD <= 1
    def height(self, node):
        if not node:
            return 0 
        return 1 + max(self.height(node.left), self.height(node.right))