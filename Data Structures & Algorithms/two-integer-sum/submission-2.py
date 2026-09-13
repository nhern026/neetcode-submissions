# Session 3, attempt 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val2id = {}

        for idx, val in enumerate(nums):
            compliment = target - val 
            if compliment in val2id:
                return [val2id[compliment], idx]
            else:
                if val not in val2id:
                    val2id[val] = idx
        
        return [-1, -1]