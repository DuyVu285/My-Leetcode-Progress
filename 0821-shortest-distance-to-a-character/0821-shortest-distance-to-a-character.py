class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        result = [0] * n
        prev_occurrence = float('-inf')

        # Iterate forward through the string to find distances to the left of each occurrence of c
        for i in range(n):
            if s[i] == c:
                prev_occurrence = i
            result[i] = abs(i - prev_occurrence)

        prev_occurrence = float('inf')

        # Iterate backward through the string to find distances to the right of each occurrence of c
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev_occurrence = i
            result[i] = min(result[i], abs(i - prev_occurrence))

        return result