class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # understand
        # we get a string s and an array of strings words
        # return the number of words[i] that is a subsequence of s meaning 
            # check if words[i]'s chars exist in s in the same order... - can skip things so 

        # matching - one pointer

        # TLE SOLUTION: # 
        # count = 0
        # for word in words:
        #     string_ptr = 0
        #     word_ptr = 0
        #     while string_ptr < len(s) and word_ptr < len(word):
        #         if word[word_ptr] == s[string_ptr]:
        #             word_ptr += 1

        #         string_ptr += 1
        #     if word_ptr == len(word):
        #         count += 1                    

        # return count 
        # --- #

        # optimize because we can't go through string multiple times because we get a TLE
        # iterate through only once by tracking all words at once 
        # to do this, we need a hashmap that tracks "letter" --> words starting with that letter 
        dictionary = defaultdict(list)
        for word in words: # O(N)
            dictionary[word[0]].append(word) 

        count = 0
        for char in s: 
            # update dictionary based on word 
            updateWords = dictionary[char]
            dictionary[char] = []
            for w in updateWords: 
                w = w[1:]
                if len(w) == 0: 
                    count += 1
                else: 
                    # update where it goes
                    dictionary[w[0]].append(w)
        return count
        