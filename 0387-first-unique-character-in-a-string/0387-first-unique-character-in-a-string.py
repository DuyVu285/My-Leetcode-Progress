class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_freq = {}
    
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        for i, char in enumerate(s):
            if char_freq[char] == 1:
                return i

        return -1
        
            