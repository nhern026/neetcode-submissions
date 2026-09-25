# Session 1, attempt 1: i tried using set and removing the nums as i went
# BUT that wouldn't work if the start of the sequence came after a number in that sequence
# THERFORE, it is better to do this apporach
    # check if the number is a start of a sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0
        for n in nums_set:
            length = 0
            if n - 1 not in nums_set: # wowzers
                curr = n
                while curr in nums_set:
                    curr += 1
                    length += 1
                max_length = max(max_length, length)

        return max_length