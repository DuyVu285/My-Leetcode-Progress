class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def convertUpper(string):
            return string.lower()
        
        def isPalindrome(string):
            return string == string[::-1]
        
        result = re.sub('[\W_]+', '', s)
        result = convertUpper(result)
        print(result)
        return isPalindrome(result)