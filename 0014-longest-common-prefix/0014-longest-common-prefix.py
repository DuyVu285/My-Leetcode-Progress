class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = ""
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            first_char = strs[0][i]
            if all(word[i] == first_char for word in strs):
                prefix += first_char
            else:
                break

        return prefix
                