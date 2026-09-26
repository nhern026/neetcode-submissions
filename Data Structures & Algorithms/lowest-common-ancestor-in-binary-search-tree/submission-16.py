# Session 3, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findSplit(curr):
            if p.val < curr.val and q.val < curr.val:
                return findSplit(curr.left)
            elif p.val > curr.val and q.val > curr.val:
                return findSplit(curr.right)
            else:
                return curr

        return findSplit(root)