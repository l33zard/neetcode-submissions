# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        q = deque([[root, 0]])
        while q:
            node, depth = q.popleft() 
            maxD = max(depth, maxD)
            if node:
                q.append([node.left, 1 + depth]) 
                q.append([node.right, 1 + depth]) 
        return maxD
                