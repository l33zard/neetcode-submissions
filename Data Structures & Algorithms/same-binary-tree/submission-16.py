# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        P = deque([p])
        Q = deque([q])
        while P and Q:
            nodeP = P.popleft()
            nodeQ = Q.popleft()
            if not nodeP and not nodeQ:
                continue
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False
            P.append(nodeP.left)
            P.append(nodeP.right)
            Q.append(nodeQ.left)
            Q.append(nodeQ.right)
        return True