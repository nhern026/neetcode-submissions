# Session 2, attempt 1
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0]), #height vals are >= 0
        TRANS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        pSet = set()
        aSet = set()
        res = []
        
        def dfs(r, c, oceanSet):
            if ((r, c)) in oceanSet:
                return 
            
            oceanSet.add((r,c))

            # explore
            for t in TRANS:
                new_r = r + t[0]
                new_c = c + t[1]
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    if heights[new_r][new_c] >= heights[r][c]:
                        dfs(new_r, new_c, oceanSet)

        # search from top and bottowm rows
        for c in range(COLS):
            dfs(0, c, pSet)
            dfs(ROWS-1, c, aSet)
        
        # search from left and right cols
        for r in range(ROWS):
            dfs(r, 0, pSet)
            dfs(r, COLS-1, aSet)

        # loop through all cells and add to res if in both sets!
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in aSet and (r,c) in pSet:
                    res.append([r, c])

        return res