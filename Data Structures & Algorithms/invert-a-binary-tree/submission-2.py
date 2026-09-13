# Session 3, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs_invert(curr):
            if not curr:
                return
            
            dfs_invert(curr.left)
            dfs_invert(curr.right)

            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            return # don't need but i like

        dfs_invert(root)

        return root