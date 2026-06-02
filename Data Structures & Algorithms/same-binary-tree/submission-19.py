# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qP = deque([p])
        qQ = deque([q])
        while qP and qQ:
            nP = qP.popleft()
            nQ = qQ.popleft()
            if not nP and not nQ:
                continue 
            if not nP or not nQ or nP.val != nQ.val:
                return False 
            qP.append(nP.left)
            qP.append(nP.right)
            qQ.append(nQ.left)
            qQ.append(nQ.right)
        return True