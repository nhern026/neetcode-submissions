# Session 2, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        valHolder = []

        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.right)
            valHolder.append(curr.val)
            dfs(curr.left)

            return 
        
        dfs(root)
        
        res = -1
        for _ in range(k):
            res = valHolder.pop()

        return res

        
