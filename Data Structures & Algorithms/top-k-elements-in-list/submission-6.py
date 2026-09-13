#session 2, attemp 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqs stores the unique value of the numbers in nums
        #   it uses the count of that number as the id and has the value within a list in 
        #   that "bucket"
        freqs =[[] for _ in range(len(nums)+1)]

        # counts is just a dict that stores {number: count}
        counts = Counter(nums)
        # Counter(nums) is the same as this code: its a python dict for counting
        # for n in nums:
        #     counts[n] = 1 + counts.get(n, 0)

        # here we are going throguh all the numbers (unique) in our dict and inserting it 
        #   into the appropiate place in freqs
        for number, freq in counts.items():
            freqs[freq].append(number)
        
        # here is the final logic where we collect numbers in res until we hit k. 
        #   we work backwards ensuring k most are found. 
        res = []
        idx = len(nums)
        while len(res) != k:
            for number in freqs[idx]:
                res.append(number)
                if len(res) == k:
                    return res
            idx -= 1
        
        return res

