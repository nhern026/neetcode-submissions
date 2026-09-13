# Session 1, attempt 2: NEETCODE

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        neighbor_transformations = [(-1, 0), (1, 0), (0, -1), (0, 1)]  


        def dfs(r, c, visit, prevHeight):
            if((r, c) in visit or not((0 <= r < ROWS and (0 <= c < COLS))) or heights[r][c] < prevHeight):
                return
            visit.add((r,c))

            for transform in neighbor_transformations:
                new_r = r + transform[0]
                new_c = c + transform[1]
                dfs(new_r, new_c, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # prevHeight = heights[r][c] for now
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])

        return res