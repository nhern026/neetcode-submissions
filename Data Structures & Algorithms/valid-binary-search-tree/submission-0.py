# session 1, attempt 2: 
#basically at each node ask: you can be any val bewteen these two numbers. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(curr, left, right):
            if not curr:
                return True
            
            if curr.val > left and curr.val < right:
                return isValid(curr.left, left, curr.val) and isValid(curr.right, curr.val, right)
            else:
                return False

        return isValid(root, -math.inf, math.inf)