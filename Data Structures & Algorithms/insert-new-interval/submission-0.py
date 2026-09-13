# Session 1, attempt 2: neetcode video
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            # first two coniditions are for non overlapping
            if newInterval[1] < intervals[i][0]: # if it comes before
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # if it comes after
                res.append(intervals[i])
            else: # if it overlaps
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res

        