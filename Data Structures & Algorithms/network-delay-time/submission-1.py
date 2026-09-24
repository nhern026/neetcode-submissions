# Session 1,attempt 1: came in knowing its djikstra's
# wegihtd == djikstra's.

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distHeap = [] # heap that stores [time to get to node, node]
        min_times = defaultdict(int) # node : min time so far
        adjacencyMap = defaultdict(list) # node : [[dst, weight/time], [dst, time]]

        # build adjacency list for O(1) look up times later
        for src, dst, ti in times:
            adjacencyMap[src].append([dst, ti])

        # build initial queue (only starting node) and min_times dictionary (full)
        for node in range(n):
            if node+1 == k:
                distHeap.append([0, node+1])
                min_times[node+1] = 0
            else:
                min_times[node+1] = math.inf

        # PERFORM THE UPDATES
        visited_nodes = set()
        while distHeap:
            _, curr = heapq.heappop(distHeap)
            if curr not in visited_nodes:
                # min_times[curr] = time_to_curr

                for dst, ti in adjacencyMap[curr]: # for each edge
                    if min_times[dst] > ti + min_times[curr]: # if the new time is smaller
                        # update it!
                        min_times[dst] = ti + min_times[curr]
                        # add it to new time to queue now!
                        heapq.heappush(distHeap, [min_times[dst], dst])
        
        # ret the time to get to the furthest node. if a node can't be reached: ret -1
        max_time = -1
        for src, ti in min_times.items():
            max_time = max(max_time, ti)
        return max_time if max_time < math.inf else -1