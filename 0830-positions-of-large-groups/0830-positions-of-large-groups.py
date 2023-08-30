class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        start = 0
        end = 0

        for i in range(1, len(s)):
            if s[i] == s[end]:
                end = i
            else:
                if end - start + 1 >= 3:
                    result.append([start, end])
                start = i
                end = i

        if end - start + 1 >= 3:
            result.append([start, end])

        return result