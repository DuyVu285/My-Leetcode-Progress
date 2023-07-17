class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            result.append(self.CountOnes(i))
            
        return result
        
    def CountOnes(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count