# Session 2, attempt 1: morning after, just trying to do it from memory
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        

        def find(x):
            while x != parent[x]: # while not representative / root
                parent[x] = parent[parent[x]] # flatten by 1
                x = parent[x]
            
            return x

        def union(a, b):
            root_a = find(a) # think why find?
            root_b = find(b)

            if root_a == root_b:
                return False

            parent[root_b] = parent[root_a] # think why roots here
            return True



        # are they all connceted ? 
        if len(edges) != n-1: # 
            return False


        # are there no cycles ?
        for a, b in edges:
            if not union(a, b):
                return False


        

        return True