class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = []
        spaces_set = set(spaces)
        n = len(s)
        for i in range(n):
            if i in spaces_set:
                new_s.append(' ')
            new_s.append(s[i])
        return ''.join(new_s)