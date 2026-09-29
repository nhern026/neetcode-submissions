# Session 1, attempt 3: claude
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(curr):
            if curr is None:
                return None
            if curr is p or curr is q:
                return curr

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr

            return left if left is not None else right
                # askign if left is not None checks against None
                # asking if left is just checking if left is truthy (which it is unless it redefines __bool__ or __len__)

        return dfs(root)