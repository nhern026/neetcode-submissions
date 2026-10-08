# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p = 1
        # q = 2
        def dfs(curr):
            if not curr:
                return None

            if curr == p or curr == q:
                return curr

            found_on_left = dfs(curr.left)
            found_on_right = dfs(curr.right)

            if found_on_left and found_on_right:
                return curr # lowest common ancestor

            if found_on_left or found_on_right:
                if found_on_right:
                    return found_on_right
                return found_on_left
            
            return None
            

        return dfs(root)

"""
p = 1, q = 2 --> 3
p = 1, q = 3 --> 3
p = 4, q = 2 --> 5

                
                    5(2 and 4)
            3(2 or)               4()
        2()       1()

"""
