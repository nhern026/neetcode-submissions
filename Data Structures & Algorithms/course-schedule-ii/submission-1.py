# Session 1, attempt 1:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        courseSeen = set()

        # build adjacency list
        prereqMap = {}
        for n in range(numCourses):
            prereqMap[n] = []
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False


            visited.add(crs)
            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False

            if crs not in courseSeen:
                res.append(crs)
            courseSeen.add(crs)
            
            prereqMap[crs] = []
            visited.remove(crs)
            return True


        for n in range(numCourses):
            if not dfs(n):
                return []
        
        return res
