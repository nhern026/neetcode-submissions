# Session 1, attempt 1: neetcode video after watching explanation
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        total = 0
        
        pre = 0
        for n in nums:
            new_num = pre + n
            potential_prefix = new_num - k
            if potential_prefix in prefix_count:
                total += prefix_count[potential_prefix]
            pre = new_num
            
            prefix_count[new_num] += 1
        
        return total

