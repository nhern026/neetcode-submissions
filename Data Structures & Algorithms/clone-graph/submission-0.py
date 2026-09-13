# Session 1, attempt 1: 9:55 PM
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
        
        def copy_cat(curr):
            curr_copy = Node(curr.val, []) # neighbor = None
            real2clone[curr] = curr_copy

            for child in curr.neighbors:
                if child not in real2clone:
                    curr_copy.neighbors.append(copy_cat(child))
                else:
                    curr_copy.neighbors.append(real2clone[child])
            return curr_copy

        return copy_cat(node)

