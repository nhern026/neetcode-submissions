class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unused = set()
        nums.sort()

        for n in nums:
            unused.add(n)

        max_length = 0
        for n in nums:
            length = 0
            while n in unused:
                unused.remove(n)
                n += 1
                length += 1
            max_length = max(max_length, length)

        return max_length