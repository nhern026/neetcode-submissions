# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node2parent = {}

        def dfs(curr, parent):
            if curr is None:
                return

            node2parent[curr] = parent
        
            dfs(curr.left, curr)
            dfs(curr.right, curr)

        dfs(root, None)

        ancestor_set = set()
        ancestor_set.add(p)
        
        p_parent = node2parent[p]
        while p_parent is not None:
            ancestor_set.add(p_parent)
            p_parent = node2parent[p_parent]
        
        if q in ancestor_set:
            return q

        q_parent = node2parent[q]
        while q_parent not in ancestor_set:
            q_parent = node2parent[q_parent]

        
        return q_parent