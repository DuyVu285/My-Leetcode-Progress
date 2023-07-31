class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("A") > 1:
            return False
        
        for i in range(len(s) - 2):
            if s[i] == "L" and s[i+1] == "L" and s[i+2] == "L":
                return False
            
        return True