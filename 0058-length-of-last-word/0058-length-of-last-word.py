class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        txt = s.split()
        lastword = txt[-1]
        return len(lastword)