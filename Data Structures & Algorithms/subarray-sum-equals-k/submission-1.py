# Session 1, attempt 1: neetcode video after watching explanation

# running sum prefix calculation. crazy crazy crazy

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        total = 0
        
        pre = 0
        for n in nums:
            pre = pre + n
            potential_prefix = pre - k
            
            if potential_prefix in prefix_count:
                total += prefix_count[potential_prefix]
            
            prefix_count[pre] += 1
        
        return total

