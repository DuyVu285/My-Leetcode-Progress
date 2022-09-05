class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = 0
        i = 0
        character = list(s)
        while(i<len(s)):
            s1 = values[s[i]]
            if (i+1 < len(s)):
                s2 = values[s[i+1]]
                if (s1 >= s2):
                    sum += s1
                    i += 1
                else:
                    sum -= s1
                    i += 1
            else:
                sum += s1
                i += 1
        return sum
            