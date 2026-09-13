# Session 3, attempt 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(A, B):
            if A and B:
                if A.val == B.val:
                    return isSameTree(A.left, B.left) and isSameTree(A.right, B.right)
                else:
                    return False
            elif not A and not B:
                return True
            else: # one of them is none and the other is real
                return False


        def dfs(curr):
            if not curr:
                return False
            if isSameTree(curr, subRoot):
                return True
            else:
                return dfs(curr.left) or dfs(curr.right)


        return dfs(root)