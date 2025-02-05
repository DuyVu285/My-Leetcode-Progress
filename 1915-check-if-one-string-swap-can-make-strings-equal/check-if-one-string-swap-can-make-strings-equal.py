class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        set_s1 = set(s1)
        set_s2 = set(s2)
        if set_s1 != set_s2:
            return False
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return True if count == 0 or count == 2 else False