# Session 1, attempt 2: with no heap!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        valHolder = []

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            valHolder.append(curr.val)
            dfs(curr.right)

        dfs(root)

        for _ in range(k):
            res = valHolder.pop(0)
        
        return res