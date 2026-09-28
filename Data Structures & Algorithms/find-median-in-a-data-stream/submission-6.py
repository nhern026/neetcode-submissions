# Session 1, atttempt 1: i think i read soemhwere b4 about using two heaps or something
import heapq

class MedianFinder:

    def __init__(self):
        self.left_max_heap = [] # store neg of original values
        self.right_min_heap = []
        
    def addNum(self, num: int) -> None:
        if len(self.right_min_heap) == 0 or num >= self.right_min_heap[0]:
            heapq.heappush(self.right_min_heap, num)
            if len(self.right_min_heap) == len(self.left_max_heap) + 2: # unbalanced
                right_root = heapq.heappop(self.right_min_heap)
                heapq.heappush(self.left_max_heap, -right_root)
        elif len(self.left_max_heap) == 0 or num < self.right_min_heap[0]:
            heapq.heappush(self.left_max_heap, -num)

            if len(self.right_min_heap) == len(self.left_max_heap) - 1: # unbalanced
                left_root = -heapq.heappop(self.left_max_heap)
                heapq.heappush(self.right_min_heap, left_root)
        

    def findMedian(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (self.right_min_heap[0] + -self.left_max_heap[0]) / 2.0
        else:
            return self.right_min_heap[0]
        
    
        