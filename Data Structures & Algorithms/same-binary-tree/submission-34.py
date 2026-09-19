# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = deque([[p, q]])
        while q:
            nodeP, nodeQ = q.popleft() 
            if not nodeP and not nodeQ:
                continue 
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False 
            else:
                q.append([nodeP.left, nodeQ.left]) 
                q.append([nodeP.right, nodeQ.right])
        return True