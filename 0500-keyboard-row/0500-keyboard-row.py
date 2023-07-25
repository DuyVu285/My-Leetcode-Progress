class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []

        for word in words:
            word_in_one_row = True
            row_check = -1

            for char in word.lower():
                for i, row in enumerate(rows):
                    if char in row:
                        if row_check == -1:
                            row_check = i
                        elif row_check != i:
                            word_in_one_row = False
                            break

            if word_in_one_row:
                result.append(word)

        return result