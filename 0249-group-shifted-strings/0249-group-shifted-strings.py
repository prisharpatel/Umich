class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        # group together strings that will be in the same shifting sequence 
            # to have this be true:
                # words need to be the same length
                # all the words have some pattern between them so subtract the ascii values with the ord function
        # matching - strings, hashmaps
        # pseudocode: 
            # for all str in strings, determine the pattern and see 
            # if it exists in the hashmap and 
            # add it to the hashmap if it does
        shifted = defaultdict(list)

        for s in strings:
            # find the pattern
            pattern = str()
            for i in range(len(s)-1):
                val = (ord(s[i+1]) - ord(s[i]))
                if val < 0:
                    val += 26
                pattern += str(val) 
                pattern += " "
            shifted[pattern].append(s)
        return list(shifted.values())




        # time complexity
        # O(NK) --> N is the length of strings and K is the length of the longest string


        