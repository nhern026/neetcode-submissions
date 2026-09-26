
# Session 2, attempt 1: remember to check for base case of curr == None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid_tree_checker(curr, low, high):
            if curr == None:
                return True

            if curr.val > low and curr.val < high:
                return valid_tree_checker(curr.left, low, curr.val) and  valid_tree_checker(curr.right, curr.val, high)
            else:
                return False


        
        return valid_tree_checker(root, -math.inf, math.inf)