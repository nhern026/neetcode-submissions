class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs =[[] for _ in range(len(nums)+1)]

        counts = {}
        
        
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for number, freq in counts.items():
            freqs[freq].append(number)
        
        res = []
        idx = len(nums)-1
        while len(res) != k:
            for j in range(0, len(freqs[idx])):
                res.append(freqs[idx][j])
                if len(res) == k:
                    return res
            idx -= 1
        
        return res


        # for i in range(len(nums)-1, -1, -1):
        #     print(i)


