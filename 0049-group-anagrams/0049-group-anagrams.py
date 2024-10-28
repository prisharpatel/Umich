class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagrams together
        # anagrams are words formed by rearranging same lettesr

        # matching - strings, sorting 

        # pseudocode: 
        # have a hashmap where you have ordered formulation of letters--> [] - list of all letters in a string format
        # can't use a set bc thats mutable and also if htere are double letters, wouldn't count that
        # at the end, go through hashmap values and add to an output array
         # go through list
        anagrams = defaultdict(list)
        for s in strs:
            ordered_s = sorted(s)
            ordered_s = str(ordered_s)
            anagrams[ordered_s].append(s)
       
        return list(anagrams.values())

        