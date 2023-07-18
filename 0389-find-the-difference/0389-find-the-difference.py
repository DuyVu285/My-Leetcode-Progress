class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
            
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
            
        for char in t_freq:
            if char not in s_freq or t_freq[char] > s_freq[char]:
                return char
        
        return ""