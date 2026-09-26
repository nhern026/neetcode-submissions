# Sesion 1, attempt 1: had an attempt but didn't really understand what a path is in this problem. but i got very close. it is indeed similar to diamater of binary tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf

        def dfs(curr): # update max_sum 
            nonlocal max_sum

            if curr == None:
                return 0

            left_sum = dfs(curr.left)
            right_sum = dfs(curr.right)
            kids_sum = max(left_sum, right_sum, left_sum + right_sum)

            # if this is pivot point: 
            max_sum = max(max_sum, curr.val + kids_sum, curr.val)

            # send up to parent, can only choose left or right then (because this is not pivot)
            curr_sum = max(curr.val, curr.val + left_sum, curr.val + right_sum)
            return curr_sum

        dfs(root)
        return max_sum