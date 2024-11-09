class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # return max length of sub array summing to k
        # prefix sum hashmap 
        # map storing prefix sum --> earliest sub array index so that it creates the largest expansion
        # need to have a bc of 0--> 1 bc that subarray is one that counts 
        # to get max size - need to iterate over all of the options and decide which ones
        # 
        prefixSum = {0:1} 
        # calculate prefix sums as you go over it and you only need O(n) because prefix sum will act as a left pointer almost??
        maxSize = 0
        curSum =0 
        for i in range(len(nums)):
            curSum += nums[i] 
            check = curSum - k 

            # if the one we are looking at sums to k 
            if curSum == k: 
                maxSize = i + 1
            if check in prefixSum: 
                # check indices length 
                maxSize = max(maxSize, i - prefixSum[check])
            # only want to add if it DNE bc otherwise adding index that is too far to the right than 
            # the longest option
            if curSum not in prefixSum:
                prefixSum[curSum] = i
        return maxSize 



        