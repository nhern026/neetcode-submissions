# Session 3, attempt 1:


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        okay because our integers in nums could be negative, we can't do sliding window
            if it was only nonnegative then we would know that that adding another number would make it not decrease. so then we could keep extening until we make it up to k, then shrink as long as we are still k
        
        so instead we can use prefix sum here since we have a goal in mind. 

        [1, 2, 0, 4, 5] k=4
        [1, 3, 3, 7, 15] k=4

        by holding the prefixes we could easily tell if any and how many subarray's before it equal our target. then our valid subarrays exist between those indices and the current one we're at

        so we need a 
        hashmap to old prefix vals and counts
        O(n)
        
        and we'll scan through each index and say that's the last number in our subarray and then have an O(1) check to see how many subarrays we can make. meanwhile we'll be adding the running usm to our prefix map
        """
        
        prefix2count = {}
        prefix2count[0] = 1

        total_subarrays = 0
        running_sum = 0
        for n in nums: # r is our ending number
            running_sum += n

            target = running_sum - k
            if target in prefix2count:
                total_subarrays += prefix2count[target]

            if running_sum in prefix2count:
                prefix2count[running_sum] += 1
            else:
                prefix2count[running_sum] = 1
        
        return total_subarrays

        """
        [2,-1,1,2], k = 2, {0:1}, total = 0
        running_sum = 2, target = 0, total = 1, {0:1, 2:1}
        running_sum = 1, target = -1, total = 1, {0:1, 2:1, 1:1}
        running_sum = 2, target = 0, total = 2, {0:1, 2:2, 1:1}
        running_sum = 4, target = 2, total = 4, {0:1, 2:2, 1:1, 3:1, 4:1}

        return total = 4



        """




