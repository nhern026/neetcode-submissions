# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(A, B):
            if A is None and B is None:
                return True
            if A is None or B is None:
                return False
            if A.val != B.val:
                return False
            return isSameTree(A.left, B.left) and isSameTree(A.right, B.right)

        stack = []
        stack.append(root)

        while stack:
            curr = stack.pop()
            if isSameTree(curr, subRoot):
                return True
            else:
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        
        return False




        

        