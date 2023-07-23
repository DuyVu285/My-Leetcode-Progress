class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace("-","").upper()
        
        first_group_length = len(s) % k if len(s) % k != 0 else k
        
        reformatted_key = s[:first_group_length]
        
        for i in range(first_group_length, len(s), k):
            reformatted_key += '-' + s[i:i+k]
            
        return reformatted_key