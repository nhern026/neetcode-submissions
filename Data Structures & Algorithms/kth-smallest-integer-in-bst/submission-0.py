# Session 1, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHolder = []

        def dfs(curr):
            if not curr:
                return

            heapq.heappush(minHolder, curr.val)
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        for _ in range(k):
            res = heapq.heappop(minHolder)
        
        return res