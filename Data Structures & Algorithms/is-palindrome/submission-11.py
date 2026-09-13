class Solution:
    def isPalindrome(self, s: str) -> bool: #char.isalnum()
        i = 0
        j = len(s)-1

        while i < j and i < len(s) and j > 0:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            # print(s[i].lower(), s[j].lower())
            if (i > j) or (s[i].lower() != s[j].lower()):
                return False
            i += 1
            j -= 1

        return True
