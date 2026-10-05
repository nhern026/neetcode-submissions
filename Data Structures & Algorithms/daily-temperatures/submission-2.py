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


        
        # temp = [1, 2, 3]
        # re

        # temp = [3, 2, 1]

        # temp = [1, 3, 2]
    

        # temp = [57, 55]
        #          (55, 1)
        # stack = [(57, 0), (55, 1)
        # res = [0, 0]

        # tem = [30,38,30,36,35,38,28]
        # res = [0, 0, 0, 0, 0, 0, 0]
        # stk = [(30, 0), 
        #        (38, 1)

        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if stack: 
                curr = stack[-1] # the last element in stack
                while stack and curr[0] < temperatures[i]:
                    result[curr[1]] = i - curr[1]

                    stack.pop()
                    if stack:
                        curr = stack[-1]
            
            stack.append((temperatures[i], i))

        return result

        # (val, i)
        # (40, 7)
        # stack = [(38, 1), (40, 7)
        # time complexity = O(n)

        # [30,38,30,36,35,38,28, 40]
        # [1, 6, 1, 2, 1, 2, 1, 0]
        # brute force --> O(n^2)
