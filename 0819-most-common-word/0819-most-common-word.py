class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # understand
        # given a paragraph and an array of banned words, return most frequent word not in banned
        # Q: what is defined as a word, something guaranteed to be split by two spaces or can it havea. comma too? 
        # A: comma - yes, so go through string checking for each char to be isAlpha 
        # Matching 
            # hashmap, sets, going through strings

        # pseudocode
        # declarehashmap
        # convert banned into set so O(1) access when searching inside of it 
        # go through paragraph with two while loops to find word (second while loop is fastforwarding until a nonAlpha character)
        # --> still O(n) bc only accesing each element 1x 

        # with word, store in hashmap if it is not in banned, if in banned, ignore it
        # return max word of hashmap 

        mostCommon = defaultdict(int) # starts with 0 everytime for every key added: word --> # appearances
        bannedSet = set(banned) # O(n) bc insert to set is O(1) and doing this n times

        pos = 0
        while pos < len(paragraph):
            while pos < len(paragraph) and not paragraph[pos].isalpha():
                pos += 1
            start = pos
            while pos + 1 < len(paragraph) and paragraph[pos+1].isalpha():
                pos += 1
            word = paragraph[start:pos+1]
            word = word.lower()
            if word not in bannedSet:
                # add to hashmap
                mostCommon[word] += 1
            pos += 1
            
        
        # find  key associated with maximum value in hashmap 
        # Q: guaranteed to be unique? --A: yes

        max_key = max(mostCommon, key=lambda k: mostCommon[k])
        return max_key

            
        