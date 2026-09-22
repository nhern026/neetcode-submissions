# Session 2, attempt 1: 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not Node:
            return []

        id2Node = {}
        visited = set()
        def dfs(curr):
            if curr is None:
                return None
            
            currCopy = Node(curr.val)
            id2Node[currCopy.val] = currCopy # id 1 indexes to real node 1
            visited.add(curr.val)

            for neighbor in curr.neighbors:
                if neighbor.val in visited:
                    id2Node[curr.val].neighbors.append(id2Node[neighbor.val])
                else:
                    id2Node[curr.val].neighbors.append(dfs(neighbor))

            return currCopy
        
        return dfs(node)

