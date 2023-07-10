class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = num
        while len(str(result)) > 1:
            answer = 0
            for i in str(result):
                answer += int(i)
            result = answer
        
        return result
                