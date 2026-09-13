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
            print(curr.val)
            if not curr:
                return
            if p.val < curr.val and q.val < curr.val:
                findSplit(curr.left, p, q)
            elif p.val > curr.val and q.val > curr.val:
                findSplit(curr.right, p, q)
            else:
                self.res = curr
        
        findSplit(root, p, q)
        return self.res