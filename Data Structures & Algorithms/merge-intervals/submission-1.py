# Session 2, attempt 1: 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort() # need to sort to get all starting times in order
        res = []

        # intervals = [[1,3],[1,5],[6,7]]
        curr_interval = intervals[0]
        for i in range(1, len(intervals)):
            next_interval = intervals[i]

            if curr_interval[1] >= next_interval[0]:
                curr_interval[0] = min(curr_interval[0], next_interval[0])
                curr_interval[1] = max(curr_interval[1], next_interval[1])
            else:
                res.append(curr_interval)
                curr_interval = next_interval

        res.append(curr_interval)
        return res