class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # words consists of dif strings
        # words[i] and words[j] paired 
            # iff words[j][::-1] = words[i]
        # return number of pairs 

        # matching - arrays, two pointer, pairs??
        
        # pseudocode -
        # create word set - since they are distinct
        # go through words and see if opposite exists in word set, divide by 2 at end bc
        # everything will have been added two times
        wordSet = set(words) # O(N)
        count = 0
        for word in words:
            if word[::-1] in wordSet and word != word[::-1]:
                count += 1
        return floor(count / 2)


        