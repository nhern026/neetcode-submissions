class Solution:
    # bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_freqID = [[] for _ in range(len(nums)+1)]

        count_dict = {}

        for x in nums:
            count_dict[x] = 1 + count_dict.get(x, 0)
        
        for val, count in count_dict.items():
            counts_freqID[count].append(val)
        
        res = []
        for i in range(len(nums), 0, -1):
            if len(res) == k:
                return res
            res +=  counts_freqID[i]
        return res
            