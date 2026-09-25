# Session 2, attempt 1: 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixes = defaultdict(int)
        prefixes[0] = 1

        running_sum = 0
        for n in nums: 
            running_sum += n
            
            count += prefixes.get(running_sum - k, 0) # key here is to look for running_sum - k (essentially what we need to make this subarray equal k)
            prefixes[running_sum] += 1
        
        return count
