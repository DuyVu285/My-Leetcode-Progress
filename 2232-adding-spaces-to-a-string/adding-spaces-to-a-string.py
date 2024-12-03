class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = []
        spaces_set = set(spaces)
        n = len(s)
        index = 0
        spaces_len = len(spaces)
        for i in range(n):
            if index < spaces_len and i == spaces[index]:
                new_s.append(' ')
                index += 1
            new_s.append(s[i])
        return ''.join(new_s)