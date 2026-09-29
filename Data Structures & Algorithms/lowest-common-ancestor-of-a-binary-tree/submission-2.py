# Session 1, attempt 2: after reading quickly through solution. really shoudl have been able to get this
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res = None

        def dfs(curr):
            if not curr:
                return False

            in_left = dfs(curr.left)
            in_right = dfs(curr.right)

            if (curr == p or curr == q) and (in_left or in_right):
                self.res = curr
            elif in_left and in_right:
                self.res = curr
            
            if curr == p or curr == q:
                return True
            return (in_left or in_right)
        
        dfs(root)
        return self.res

