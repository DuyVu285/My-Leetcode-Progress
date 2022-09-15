class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for x in s:
            if x not in hash:
                hash.add(x)
            else:
                hash.remove(x)
        "len(hash) is the number of odd letters"
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
        