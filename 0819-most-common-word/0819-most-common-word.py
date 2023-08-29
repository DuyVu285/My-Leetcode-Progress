class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = re.findall(r'\w+', paragraph.lower())
    
        # Create a counter for the frequency of each word
        word_count = collections.Counter(words)

        # Remove banned words from the counter
        for banned_word in banned:
            word_count[banned_word.lower()] = 0

        # Find the most common word
        most_common = max(word_count, key=word_count.get)

        return most_common