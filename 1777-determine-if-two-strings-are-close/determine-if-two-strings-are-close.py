class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_set = set(word1)
        word2_set = set(word2)
        if word1_set != word2_set:
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        values_word1 = list(freq1.values())
        values_word2 = list(freq2.values())
        values_word1.sort()
        values_word2.sort()
        if values_word1 != values_word2:
            return False
        return True
        