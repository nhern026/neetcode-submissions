# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res = None

        def dfs(curr):
            if self.res: # weird way to stop it
                return False
            if not curr:
                return False
            print(curr.val)


            in_left = dfs(curr.left)
            in_right = dfs(curr.right)

            if (curr == p or curr == q) and (in_left or in_right):
                self.res = curr
            elif in_left and in_right:
                self.res = curr
            
            if curr == p or curr == q:
                return True
            return (in_left or in_right)
        
        dfs(root)
        print(self.res)
        return self.res

