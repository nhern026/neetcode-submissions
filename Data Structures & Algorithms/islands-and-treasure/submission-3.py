# Session 1, attempt 2: bfs bc dfs doesn't give us shortest distance. has to be simultaneous, or else repeated work
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we can modify grid in place
        rows, cols = len(grid), len(grid[0])
        level = 0
        queue = deque()
        visited = set()


        def is_valid(r, c):
            if (0 <= r < rows and 0 <= c < cols) and ((r,c) not in visited) and grid[r][c] > 0:
                return True
            else:
                return False

        # how do we do visited???
        def bfs():
            while queue:
                nonlocal level

                len_queue = len(queue)
                for _ in range(len_queue):
                    curr_r, curr_c = queue.popleft()
                    grid[curr_r][curr_c] = min(grid[curr_r][curr_c], level)

                    for transform in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        new_r = curr_r + transform[0]
                        new_c = curr_c + transform[1]

                        if is_valid(new_r, new_c):
                            # print(grid[new_r][new_c])
                            queue.append((new_r, new_c))
                            visited.add((new_r, new_c))
                level += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        bfs()



                    