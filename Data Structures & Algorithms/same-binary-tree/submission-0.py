# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#   same structure and same value == same tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare(A, B):
            if (A is None) and (B is None): # both are None
                return True
            if (A is None or B is  None or A.val != B.val): #1 is None or vals don't match
                return False
            else: #values match and neihter are none. 
                return (compare(A.left, B.left) and compare(A.right, B.right))
        


        return compare(p, q)