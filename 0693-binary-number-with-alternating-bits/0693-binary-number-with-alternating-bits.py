class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_bit = n % 2
        n //= 2

        while n > 0:
            current_bit = n % 2
            if current_bit == prev_bit:
                return False
            prev_bit = current_bit
            n //= 2
        
        return True