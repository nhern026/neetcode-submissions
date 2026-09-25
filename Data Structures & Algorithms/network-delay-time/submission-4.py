# Session 2, attempt 1: 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build edge list
        node2edges = defaultdict(list)
        for src, dst, ti in times:
            node2edges[src].append([dst, ti])
        
        # build min time holder 
        node2time = {}
        for node_id in range(n):
            node2time[node_id+1] = math.inf
        node2time[k] = 0

        # initialize heap
        min_time_heap = []
        heapq.heappush(min_time_heap, [0, k])

        seen = set()
        while min_time_heap:
            trail_time, curr = heapq.heappop(min_time_heap)
            if curr not in seen:
                # update kids and add to heap
                for dst, ti in node2edges[curr]:
                    node2time[dst] = min(node2time[dst], trail_time + ti)
                    heapq.heappush(min_time_heap, [node2time[dst], dst])

                # add curr from seen
                seen.add(curr)
        
        max_time = 0
        for node, time in node2time.items():
            max_time = max(max_time, time)
        
        return max_time if max_time < math.inf else -1

        