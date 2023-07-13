class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        if n % 4 == 0:
            return self.isPowerOfFour(n // 4)
        
        if n == 1:
            return True
        
        return False