class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2ID = {}

        for idx, value in enumerate(nums):
            compliment = target - value

            if compliment in val2ID:
                return [val2ID[compliment], idx]
            else:
                val2ID[value] = idx
        
        return [-1, -1]


