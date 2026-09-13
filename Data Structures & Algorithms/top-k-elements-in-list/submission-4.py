class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqs stores the unique value of the numbers in nums
        #   it uses the count of that number as the id and has the value within a list in 
        #   that "bucket"
        freqs =[[] for _ in range(len(nums)+1)]

        # counts is just a dict that counts up 
        counts = Counter(nums)
        
        # for n in nums:
        #     counts[n] = 1 + counts.get(n, 0)

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

