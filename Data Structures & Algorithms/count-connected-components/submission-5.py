class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = []
        for i in range(n):
            parent.append(i)

        def find(curr):
            while parent[curr] != curr:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]

            return curr

        def union(a, b):
            # print(parent)
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b: # if not connected yet
                parent[root_b] = root_a

            # print(parent)
            # print()
        for a, b in edges:
            union(a, b)
        
        component = 0
        for i, root in enumerate(parent):
            if i == root:
                component += 1

        return component



                    