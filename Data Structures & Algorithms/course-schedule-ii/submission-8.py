# Session 3, attempt 1:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0 --> numCourses-1
        0, 1, 2 -- if numCourses == 3

        [[1,0]] means 1 --> 0     crs --> pre

        if cycle: 
            1--> 0
            0 --> 1
            --> return []
        else;
            return valid ordering [0,1,2]

        i'm thinking of running a dfs with cycle detection using 2 sets to track fully visited nodes, nodes in the current path (will be our cycle detection), and then finally we can append to our results once we explore all of those courses prereqs. return false if any cycle is found

        0, 1, 2, 3

        0
        1 --> 2
        2 --> 0
        3
        [0, 2, 1, 3]

        """

        # build adjacency map
        crs2pre = defaultdict(list)
        for crs, pre in prerequisites:
            crs2pre[crs].append(pre)

        def dfs(crs, path=None):
            if path is None:
                path = set()
            if crs in visited:
                return True
            if crs in path:
                return False

            # visit pre's, if we make it back to this crs again we should return False (cycle)
            path.add(crs)
            for pre in crs2pre[crs]:
                if not dfs(pre, path):
                    return False
            
            # done visiting all pre's
            res.append(crs) 
            path.remove(crs)
            visited.add(crs)
            return True

        # for each course run dfs (with shared visited set across all, and unique path sets for each)
        res = []
        visited = set()
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

        """
        0 --> 1
        1 --> 2
        2 --> 0

        """
