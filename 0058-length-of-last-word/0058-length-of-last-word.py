class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return length of the last word in the string starting from the back
        n = len(s) - 1

        count = 0
        while s[n] == ' ':
            n -= 1
        while s[n] != ' ' and n >= 0:
            count += 1
            n -= 1
        return count
        

        