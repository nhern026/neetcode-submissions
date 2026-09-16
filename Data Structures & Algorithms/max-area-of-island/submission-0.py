# Session 1, attempt 1: DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbor_transformation = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        #                            up,    down,   right,  left
        maxArea = 0

        visited = set()

        def dfs(r, c): # return the size of the island 
            if (r, c) in visited: # don't double count
                return 0
            elif not (0 <= r < len(grid) and 0 <= c < len(grid[r])):
                return 0
            elif grid[r][c] == 0:
                return 0

            visited.add((r,c))

            areaOfChildren = 0
            for transform in neighbor_transformation:
                new_r = r + transform[0]
                new_c = c + transform[1]
                areaOfChildren += dfs(new_r, new_c)

            return areaOfChildren + 1 # + 1 is to count itself


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea