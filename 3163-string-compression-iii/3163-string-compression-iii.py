class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        count = 1
        comp = ""
        character = word[0]
        for i in range(1,len(word)):
            if word[i] == character and count < 9:
                count += 1
            else:
                comp += str(count) + character
                character = word[i]
                count = 1
                
        comp += str(count) + character
        return comp