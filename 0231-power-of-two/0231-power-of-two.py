class Solution(object):
    def Log2(self, x):
        if x == 0:
            return False

        return (math.log10(x) / math.log10(2))

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n < 0:
            return False
        
        return (math.ceil(self.Log2(n)) == math.floor(self.Log2(n)))