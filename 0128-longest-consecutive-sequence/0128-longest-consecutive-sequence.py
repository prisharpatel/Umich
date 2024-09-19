class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet: # means that we can check for a longer sequence already starting at num  bc if it is in numSet, we already checked for it
                currentStreak = 1
                currentNum = num

                while (currentNum + 1) in numSet:
                    currentStreak += 1
                    currentNum += 1
                if currentStreak > longest:
                    longest = currentStreak
        
        return longest
        