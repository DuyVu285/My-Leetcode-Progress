class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowel = ["a","e","i","o","u"]
        words = sentence.split()
        result = []
        
        for i, word in enumerate(words):
            if word[0].lower() in vowel:
                new_word = word + "ma" + "a" * (i+1)
            else:
                new_word = word[1:] + word[0] + "ma" + "a" * (i+1)
            
            result.append(new_word)
            
        return ' '.join(result)