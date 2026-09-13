# Session 1, attempt 1

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # return -1 when there is at least one fresh fruit 

        # return 0 when there are no fruit

        # return x when there are fruit and there is a rotten fruit in every island

        fresh_fruit_set = set()
        infected_queue = deque([])

        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_fruit_set.add((r,c))
                elif grid[r][c] == 2:
                    infected_queue.append((r,c, 0))
        
        print(infected_queue)

        # bfs
        neighbor_transformation = [(-1, 0), (0, -1), (1, 0), (0,1)]
        while infected_queue:
            rotten_fruit = infected_queue.popleft()
            rotten_r = rotten_fruit[0]
            rotten_c = rotten_fruit[1]
            rotten_t = rotten_fruit[2]

            for transform in neighbor_transformation:
                new_r = rotten_r + transform[0]
                new_c = rotten_c + transform[1]
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    if (new_r, new_c) in fresh_fruit_set:
                        fresh_fruit_set.remove((new_r, new_c))
                        infected_queue.append((new_r, new_c, rotten_t+1))
                        time = max(time, rotten_t+1)

        # only go to neighbor if fresh fruit 
        if not fresh_fruit_set:
            return time
        else:
            return -1