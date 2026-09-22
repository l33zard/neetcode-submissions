# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]
        while stack:
            nP, nQ = stack.pop() 
            if not nP and not nQ:
                continue 
            elif nP and nQ and nP.val == nQ.val:
                stack.append([nP.left, nQ.left]) 
                stack.append([nP.right, nQ.right]) 
            else:
                return False 
        return True 