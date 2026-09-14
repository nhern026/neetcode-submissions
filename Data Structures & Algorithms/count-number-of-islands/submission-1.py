# Session 2, attempt 1: 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbor_transformation = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        islandCount = 0

        visited = set()


        def island_dfs(r, c):
            visited.add((r,c))

            for transform in neighbor_transformation:
                new_r = r + transform[0]
                new_c = c + transform[1]

                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[new_r]):
                    if (new_r, new_c) not in visited:
                        if grid[new_r][new_c] == "1":
                            island_dfs(new_r, new_c) 



        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island_dfs(r, c)
                    islandCount += 1
        
        return islandCount