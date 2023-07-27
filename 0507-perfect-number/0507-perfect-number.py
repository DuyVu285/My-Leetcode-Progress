class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        numsum = 1
        
        i = 2
        while i * i <= num:
            if num % i == 0:
                numsum = numsum + i + num/i
            i += 1
        
        return (True if numsum == num and num!=1 else False)