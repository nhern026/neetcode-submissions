# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dive(node, depth):
            if node is None:
                return depth
            
            return max(dive(node.left, depth+1), dive(node.right, depth+1))



        return dive(root, 0)