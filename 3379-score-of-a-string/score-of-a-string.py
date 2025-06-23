class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(1,n):
            result += abs(ord(s[i]) - ord(s[i-1]))
        return result
