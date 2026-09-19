# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        Q = deque([[p,q]]) 
        while Q:
            nodeP, nodeQ = Q.popleft() 
            if not nodeP and not nodeQ:
                continue 
            elif not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False 
            Q.append([nodeP.left, nodeQ.left]) 
            Q.append([nodeP.right, nodeQ.right]) 
        return True 