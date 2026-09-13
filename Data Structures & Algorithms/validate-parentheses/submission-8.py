class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        close2open = {')': '(', ']': '[', '}': '{'}
        stack = []

        for bracket in s:
            if bracket not in close2open:
                stack.append(bracket)
            else:
                if stack:
                    openBrack = stack.pop()
                    if close2open[bracket] != openBrack:
                        return False
                else:
                    return False

        if stack:
            return False
        else:
            return True
        

        