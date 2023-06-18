class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        capitalize_title = title.lower().title()
        words = capitalize_title.split()
        
        for i in range(len(words)):
            if len(words[i]) < 3:
                words[i] = words[i].lower()
                
        return ' '.join(words)
        