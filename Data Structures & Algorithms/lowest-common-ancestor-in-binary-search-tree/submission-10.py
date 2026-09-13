# Session 1, attempt 3. after watching 1.5 min of neetcode's explanation where he said "if there's a split" thats the lowest common ancestor. FAHHH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#chat says i acyually don't 
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def findSplit(curr, p, q):
            if not curr:
                return None

            if curr.val > p.val and curr.val > q.val:
                return findSplit(curr.left, p, q)
            elif curr.val < p.val and curr.val < q.val:
                return findSplit(curr.right, p, q)
            else:
                return curr
        
        return findSplit(root, p, q)
