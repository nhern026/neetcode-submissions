# Session 1, attempt 1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # return result array where i is int count of days ahead (0 if none)
        
        # temperatures = [30,38,30,36,35,40,28]
        # result example: [1,4,1,2,1,0,0]

        # is every element an int? --> yes
        # will there alwyas be a temperatures array of len >= 1? --> yes
        # how big can it get? --> VERY BIG
        # can temepreature ints be negative? --> no
        # can i modify temperatures in place if i need to? --> yes but prob don't don't need to
        
        # []

        # [30,38,30,36,35,38,28]
        # [1, 4, 1, 0, 0, 0, 0]
        # brute force --> O(n^2)

        # temp = [57, 55]
        #          (55, 1)
        # stack = [(57, 0), (55, 1)
        # res = [0, 0]

        # tem = [30,38,30,36,35,40,28]
        # res = [1, 4, 1, 2, 1, 0, 0]
        # stk = [(40, 5), (28, 6)
        #       

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                        
            stack.append((temperatures[i], i))

        return result

        # (val, i)
        # (40, 7)
        # stack = [(38, 1), (40, 7)
        # time complexity = O(n) 

        # [30,38,30,36,35,38,28, 40]
        # [1, 6, 1, 2, 1, 2, 1, 0]
        # brute force --> O(n^2)
