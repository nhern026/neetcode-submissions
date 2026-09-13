class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums): 
            if target - val not in seen: 
                seen[val] = idx
            else:
                return [seen[target - val], idx]
        
        return [-1, -1]

        
