# Session 2, attempt 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(A, B):
            if A and B:
                if A.val == B.val:
                    return dfs(A.left, B.left) and dfs(A.right, B.right)
                else:
                    return False
            elif not A and not B:
                return True
            elif (not A and B) or (A and not B):
                return False

        return dfs(p, q)