class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # goal: length of longest substring without repeating characters 
        # substring - contigious set of letters in s 

        # matching - sliding window, use a hashset to track whats in the current string or not so its O(1) access

        # pseudocode - if the letter right is pointing to is not in tracker - add it to tracker and 
        # move forward, if it is, then move left over including all letters left points to 
        # until the letter right is pointing to is not in tracker 

        tracker = set()
        left = 0
        maxSize = 0
        #output = ""
        for right in range(len(s)): 
            letter = s[right]
            if letter not in tracker: 
                tracker.add(letter)
            else: 
                # letter in tracker so we reached a substring wtihout repeating characters
                if right - left > maxSize:
                    maxSize = right-left # no need for + 1 becuase right already ahead by 1 character
                # move left pointer over
                while letter in tracker and left < right: 
                    tracker.remove(s[left])
                    left += 1
                tracker.add(letter)
        if maxSize == 0:
            return len(s)
        if right-left+1 > maxSize:
            return right-left+1
        return maxSize
        
            

        