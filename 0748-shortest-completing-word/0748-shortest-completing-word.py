import collections
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def clean_license_plate(licensePlate):
            valid_chars = set(string.ascii_letters)
            return ''.join(filter(lambda c: c in valid_chars, licensePlate)).lower()
        
        def is_completing_word(word, licensePlate_count):
            word_count = collections.Counter(word)
            for char, count in licensePlate_count.items():
                if word_count[char] < count:
                    return False
            return True
        
        cleaned_license_plate = clean_license_plate(licensePlate)
        licensePlate_count = collections.Counter(cleaned_license_plate)

        shortest_word = None
        min_length = float('inf')

        for word in words:
            if is_completing_word(word, licensePlate_count):
                if len(word) < min_length:
                    shortest_word = word
                    min_length = len(word)

        return shortest_word