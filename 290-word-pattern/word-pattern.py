class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        n = len(words)
        char_to_word = {}
        word_to_char = {}

        if len(pattern) != n:
            return False

        for i in range(n):
            char = pattern[i]
            word = words[i]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        return True
