class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1: 
            return 1
        elif len(s) == 0:
            return 0

        left, right = 0, 1
        ltrFreq = defaultdict(int) #always starts 0
        ltrFreq[s[left]] += 1
        ltrFreq[s[right]] += 1

        longest = 0
        most_freq = s[0]

        while left < len(s) and right < len(s):
            length = (right - left + 1)
            if length - ltrFreq[most_freq] > k:
                ltrFreq[s[left]] -= 1
                left += 1
                most_freq = max(ltrFreq, key=ltrFreq.get) #O(26) technically lol
            else:
                longest = max(longest,length)
                right += 1
                if right < len(s):
                    ltrFreq[s[right]] += 1

                    if ltrFreq[most_freq] < ltrFreq[s[right]]:
                        most_freq = s[right]


        return longest
            
                


