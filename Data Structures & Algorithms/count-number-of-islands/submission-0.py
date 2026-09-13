class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        neighbor_transformations = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        def dfs(i, j):
            visited.add((i, j))
            for transform in neighbor_transformations:
                new_i = i + transform[0]
                new_j = j + transform[1]
                if ((0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0]))) and ((new_i, new_j) not in visited):
                    if grid[new_i][new_j] == "1":
                        dfs(new_i, new_j)


        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (not (i, j) in visited) and (grid[i][j] == "1"):
                    dfs(i, j)
                    island_count += 1
        return island_count
        
        
