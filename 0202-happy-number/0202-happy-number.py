class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square_sum(num):
            sum = 0
            while num > 0:
                digit = num % 10
                sum += digit * digit
                num //= 10
            return sum
    
        slow = n
        fast = n

        while True:
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))

            if fast == 1:
                return True
            if fast == slow:
                return False







