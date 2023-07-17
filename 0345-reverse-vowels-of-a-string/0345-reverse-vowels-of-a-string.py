class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels_list = ["a","A","e","E","i","I","o","O","u","U"]
        while left < right:
            if s[left] not in vowels_list:
                left += 1
            elif s[right] not in vowels_list:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1  
        return "".join(s)
            