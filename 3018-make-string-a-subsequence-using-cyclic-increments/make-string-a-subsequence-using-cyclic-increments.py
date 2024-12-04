class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        char_map = {alphabet[i]: alphabet[(i + 1) % len(alphabet)] for i in range(len(alphabet))}

        left, right = 0, 0
        if len(str2) > len(str1):
            return False

        while left <  len(str1) and right < len(str2):
            if str1[left] == str2[right] or char_map[str1[left]] == str2[right]:
                right += 1
            left += 1

        return right == len(str2)
        
        