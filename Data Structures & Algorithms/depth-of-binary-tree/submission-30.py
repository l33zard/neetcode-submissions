# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 0]])
        maxDepth = 0
        while queue:
            node, depth = queue.popleft() 
            maxDepth = max(maxDepth, depth)
            if node:
                queue.append([node.left, 1 + depth])
                queue.append([node.right, 1 + depth])
        return maxDepth