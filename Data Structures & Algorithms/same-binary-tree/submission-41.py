# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([[p, q]])
        while queue:
            nP, nQ = queue.popleft() 
            if not nP and not nQ:
                continue 
            if not nP or not nQ or nP.val != nQ.val:
                return False 
            else:
                queue.append([nP.left, nQ.left])
                queue.append([nP.right, nQ.right]) 
        return True 
