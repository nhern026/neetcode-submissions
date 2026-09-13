class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        #setting up starting ltrs
        while left < len(s) and not s[left].isalnum():
                left += 1
        while right >= 0 and not s[right].isalnum():
                right -= 1

        while left < right and left < len(s) and right >= 0:
            print(s[left].lower(), s[right].lower())
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

            #udpate
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1

        return True
