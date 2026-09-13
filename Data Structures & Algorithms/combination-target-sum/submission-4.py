# Session 1, attempt 2: from chatgpt giving me rec to prune this tree a bit

class ListNode():
    def __init__(self, lineage=[], children=[]):
        self.lineage = lineage
        self.children = children


class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return []

        res = []
        seen = set()
        stack = []

        firstNode = ListNode([], nums)
        for i in range(len(nums)): 
            stack.append(ListNode([nums[i]], nums[i:]))

        while stack:
            curr = stack.pop()
            sumOfCurr = sum(curr.lineage)

            if sumOfCurr == target:
                sortedLinege = tuple(sorted(curr.lineage))
                if sortedLinege not in seen:
                    seen.add(sortedLinege)
                    res.append(list(sortedLinege))
            elif sumOfCurr < target:
                for i in range(len(curr.children)):
                    stack.append(ListNode(curr.lineage + [curr.children[i]], curr.children[i:]))
            
        
        return res


