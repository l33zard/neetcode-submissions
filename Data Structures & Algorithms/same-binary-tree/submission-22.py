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
            nodeP = qP.popleft()
            nodeQ = qQ.popleft()
            if not nodeP and not nodeQ:
                continue 
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False 
            qP.append(nodeP.left) 
            qP.append(nodeP.right) 
            qQ.append(nodeQ.left)
            qQ.append(nodeQ.right)
        if qP or qQ:
            return False 
        else:
            return True 