class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # understand 
            # we have a dictionary of words and we want to split up string s and 
            # see if it can be split up into words in that dictionary
            # edge cases word dict has overlapping words 
                # like worddict = ["grayhound", "gray", "hound"] --> string is "grayxhound"
    # worddict = ["hello, helloo"] --> string is "helloo" 
                    # lesson: have to continue going to the right until a substring is not a string in worddict
        # matching - 2 pointer problem / dp 

    
        wordSet = set(wordDict) #O(M)
        dp = [True] + [False] * len(s)
        for i in range(len(s)): # O(N)
            if dp[i]:
                for j in range(i + 1, len(s) + 1): # O(N)
                    if s[i:j] in wordSet: # O(N) String Generation
                        dp[j] = True     
        return dp[-1]
        