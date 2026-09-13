# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return True, 0

            left_balanced, left_height = dfs(curr.left)
            if not left_balanced:
                return False, -1

            right_balanced, right_height = dfs(curr.right)
            if not right_balanced:
                return False, -1

            if abs(left_height - right_height) <= 1:
                return True, (1 + max(left_height,right_height))
            else:
                return False, -1

        balanced, _ = dfs(root)
        return balanced