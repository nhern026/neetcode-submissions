# Session 2, attempt 2: doing optimal version (for time and space)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for n in num_set:
            if n-1 in num_set:
                continue
            
            curr = n
            curr_length = 0
            while curr in num_set:
                curr_length+=1
                curr = curr+1
            
            max_length = max(max_length, curr_length)

        return max_length
