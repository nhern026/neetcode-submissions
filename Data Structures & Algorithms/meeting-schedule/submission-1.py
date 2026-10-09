"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = []
        for interval in intervals:
            times.append([interval.start, interval.end])

        times.sort()

        for i in range(1, len(times)):
            prev_interval = times[i-1]
            curr_interval = times[i]
            if prev_interval[1] > curr_interval[0]:
                return False

        return True

        