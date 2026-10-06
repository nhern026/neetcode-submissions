# Session 3, attempt 1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Input: numCourses = 2, prerequisites = [[0,1], [0, 2], [1,2]]

        # all classses = [0, 1]


        # prerq <-- crs
        # 1 <-- 0

        crs2pre = defaultdict(list)

        for crs, pre in prerequisites:
            crs2pre[crs].append(pre)

        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False

            cycle.add(crs)
            for pre in crs2pre[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            return True            

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True









        