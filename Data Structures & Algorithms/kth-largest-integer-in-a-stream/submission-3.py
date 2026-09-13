import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        print(nums)
        self.stream = nums
        while len(self.stream) > k:
            heapq.heappop(self.stream)
        

    def add(self, val: int) -> int:
        if len(self.stream) >= self.k:
            heapq.heappush(self.stream, val)
            heapq.heappop(self.stream)
        else:
            heapq.heappush(self.stream, val)

        return self.stream[0]
        
