class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # return the shortest distance between the occurrence of these two words in a list
        # follow up - does a wrap around count? - no

        # matching - two pointers, minDist tracker

        minimum = len(wordsDict) - 1

        # min dist means words will be next to each other so have a prev index tracker
        prevIndex = -1
        # prevWord = ""


        for i, word in enumerate(wordsDict):
            if prevIndex == -1 and (word == word1 or word == word2): 
                prevIndex = i
            else: 
                if wordsDict[prevIndex] == word1: 
                    # check if cur word is word2
                    if word == word2: 
                        minimum = min(minimum, i - prevIndex) 
                        prevIndex = i
                    elif word == word1: 
                        prevIndex = i
                else: 
                    if word == word1: 
                        minimum = min(minimum, i - prevIndex) 
                        prevIndex = i 
                    elif word == word2: 
                        prevIndex = i

        return minimum 

                    








        