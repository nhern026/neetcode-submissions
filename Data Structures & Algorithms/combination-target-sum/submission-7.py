# Session 1, attempt 2: from chatgpt giving me rec to prune this tree a bit
    # this tree now only gets unique combos of how to get up to a number
    # once you pick a number, you can't pick any number that comes before it

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
        stack.append(firstNode)

        while stack:
            curr = stack.pop()
            sumOfCurr = sum(curr.lineage)

            if sumOfCurr == target:
                res.append(list(curr.lineage))
            elif sumOfCurr < target:
                # the pruning is here
                for i in range(len(curr.children)):
                    stack.append(ListNode(curr.lineage + [curr.children[i]], curr.children[i:]))
            
        
        return res


