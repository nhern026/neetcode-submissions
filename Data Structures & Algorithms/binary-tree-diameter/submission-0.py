# Session 1, attempt 1: neetcode video
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)
        dfs(root)
        return self.max_diameter
