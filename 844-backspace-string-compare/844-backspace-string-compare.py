class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def bsString(string):
            res = []
            for c in string:
                if c != '#':
                    res.append(c)
                else:
                    res = res[:-1]
            return res
        return bsString(s) == bsString(t)