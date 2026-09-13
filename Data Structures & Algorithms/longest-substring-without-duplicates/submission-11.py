class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        biggest_length = 0
        seen = set()

        left, right = 0, 1 
        seen.add(s[left])

        while right < len(s):  
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # okay now add it back to seen
            seen.add(s[right])

            curr_length = (right - left) + 1
            biggest_length = max(biggest_length, curr_length)

            right += 1
            
        return biggest_length
            


