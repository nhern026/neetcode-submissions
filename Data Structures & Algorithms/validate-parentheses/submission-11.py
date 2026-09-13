class Solution:
    def isValid(self, s: str) -> bool:
        paranthasesStack = []

        close2open = {')': '(', ']': '[', '}': '{'}

        '[(])'
        

        for paran in s:
            if paran not in close2open:
                paranthasesStack.append(paran)
            else:
                if (not paranthasesStack) or paranthasesStack.pop() != close2open[paran]:
                    return False
        
        if paranthasesStack:
            return False
        else:
            return True