class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = len(s.split())
        return result