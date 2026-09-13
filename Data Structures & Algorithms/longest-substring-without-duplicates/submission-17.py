# Session 3, attmept 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        follower = 0
        max_substring_length = 0

        for leader in range(len(s)): 
            while s[leader] in seen:
                seen.remove(s[follower])  
                follower += 1
            max_substring_length = max(max_substring_length, (leader - follower) + 1)
            seen.add(s[leader])
        
        return max_substring_length

