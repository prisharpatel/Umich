class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # U - return true or flase baesd on if a word is the same forwards as it is backwards
        # M - string problem with parsing
        # P - clean string
             # reverse string
             # check if equal
        # implement
        # clean string: 
        cleaned_string = (''.join(char for char in s if char.isalnum())).lower()
        reversed_string = cleaned_string[::-1]
        print(reversed_string)
        if cleaned_string == reversed_string:
            return True
        else: 
            return False
        