# Session 2, attempt 1: 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0]) # n x m
        TRANSFORMATIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        visited = set()

        # add treasure cells to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c)) # tuple saves space from list
                    visited.add((r,c))
        
        # perform BFS while updating each grid cell with the distance value
        distance = 0
        while q:
            q_len = len(q)
            
            #pop out each cell in current distance level
            for _ in range(q_len):
                curr = q.popleft()

                # update grid
                grid[curr[0]][curr[1]] = distance

                # adding all valid and non-visited neighbors
                for t in TRANSFORMATIONS:
                    new_r = curr[0] + t[0]
                    new_c = curr[1] + t[1]

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                        if not ((new_r, new_c) in visited):
                            if grid[new_r][new_c] > 0:
                                q.append((new_r, new_c))
                                visited.add((new_r, new_c))


            distance += 1

        return
            

            