# Session 2, attempt 2
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        follower = 0
        max_length = 0

        for leader in range(len(s)):
            count[s[leader]] = 1 + count.get(s[leader], 0)
            
            while (leader - follower + 1) - max(count.values()) > k:
                count[s[follower]] -= 1
                follower += 1
            max_length = max(max_length, (leader - follower + 1))

        return max_length
