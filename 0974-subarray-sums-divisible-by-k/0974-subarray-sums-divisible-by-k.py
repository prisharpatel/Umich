class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # return the number of non-empty sub arrays that have a sum divisible by k 

        # matching - hashmap, prefix sum 
        # sum of 0 --> j - sum of 0 --> i = sum of i+1 --> j 
        # if prefix sums have equal remainder when divided by k, their i+1 -> j will be divisible by k 

        
        count = 0 
        curSum = 0
        remainder_count = {0: 1}

        for num in nums:
            curSum += num
            remainder = curSum % k 

            if remainder < 0:
                remainder += k 

            if remainder in remainder_count:
                count += remainder_count[remainder] # bc we can add that subarray with the current one because the 
                # i+1 -> j array will be divisible by k 

            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        return count


            
        return count



        