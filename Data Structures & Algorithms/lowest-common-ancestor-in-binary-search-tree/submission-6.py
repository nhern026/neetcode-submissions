# Session 1, attempt 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None

        def findSplit(curr, p, q):
            if not curr:
                return 
            print(curr.val)
            if curr.val > p.val and curr.val > q.val:
                findSplit(curr.left, p, q)
            elif curr.val < p.val and curr.val < q.val:
                findSplit(curr.right, p, q)
            else:
                self.res = curr
        
        findSplit(root, p, q)
        return self.res