"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = [(0,40),(5,10),(15,20)]
        # 0                                     40
        #      5  10
        #               15   20
        
        meeting_min_heap = []

        for interval in intervals:
            start, end = interval.start, interval.end
            meeting_min_heap.append([start, 1])
            meeting_min_heap.append([end, -1])     

        heapq.heapify(meeting_min_heap)

        room_count = 0
        max_room_count = 0


        while meeting_min_heap:
            time, mod = heapq.heappop(meeting_min_heap)
            room_count += mod

            max_room_count = max(max_room_count, room_count)
            

        return max_room_count

