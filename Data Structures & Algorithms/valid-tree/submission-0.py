# Session 1, attempt 1: after 7:24 on neetcode video
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node2neighbs = {}
        for idx in range(n): #check defaultdict
            node2neighbs[idx] = []

        for curr, neighbor in edges:
            node2neighbs[curr].append(neighbor)
            node2neighbs[neighbor].append(curr)

        visited = set()
        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)

            for neighbor in node2neighbs[curr]:
                if not (neighbor == prev):
                    if not dfs(neighbor, curr):
                        return False

            return True


        return dfs(0, -1) and len(visited) == n