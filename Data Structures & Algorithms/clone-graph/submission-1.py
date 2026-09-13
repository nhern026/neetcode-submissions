# Session 1, attempt 1: 9:55 PM --> 10:20 PM. 1 hint that made me realize i should use a dictionary. 

# NEXT TIME I SOLVE THIS< DO IT CLEANER BY CHANGING THE BASE CASE IN DFS TO
# HAS THIS CLONE BEEN VISITED BEFOER????


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        real2clone = {}
        
        def dfs(curr):
            curr_copy = Node(curr.val, []) # neighbor = None
            real2clone[curr] = curr_copy

            for child in curr.neighbors:
                if child not in real2clone:
                    curr_copy.neighbors.append(dfs(child))
                else:
                    curr_copy.neighbors.append(real2clone[child])
            return curr_copy

        return dfs(node)

