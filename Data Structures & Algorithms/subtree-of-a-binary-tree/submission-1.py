#Session 1, attempt 1. had to look at some older code to work it
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(A, B):
            if A is None and B is None:
                print("both None")
                return True
            elif A is None or B is None or A.val != B.val:
                if A is None:
                    print("None ", B.val)
                elif B is None:
                    print(A.val, " None")
                else:
                    print(A.val, B.val)
                return False
            else:
                print(A.val, B.val)
                return compare(A.left, B.left) and compare(A.right, B.right)

        def findSubRoot(curr):
            if curr is None:
                return False
            if curr.val == subRoot.val:
                if compare(curr, subRoot):
                    return True
            return findSubRoot(curr.left) or findSubRoot(curr.right)
            
            
        return findSubRoot(root)