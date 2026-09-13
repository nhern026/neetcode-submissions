# Session 1, attempt 1: Neetcode Video
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to prereq list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs)
            preMap[crs] = [] #saves us work. think why
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        