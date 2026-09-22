# Session 2, attempt 1: 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build adjacency map
        prereqMap = {}
        for n in range(numCourses):
            prereqMap[n] = []
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        # dfs logic
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            
            visitSet.add(crs)
            # for each prereq for this guy:
            for pre in prereqMap[crs]:
                if pre in visitSet or not dfs(pre):
                    return False

            prereqMap[crs] = [] # gets rid of prereq list
            visitSet.remove(crs)
            return True


        # go through each class and follow its prereqs
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True


