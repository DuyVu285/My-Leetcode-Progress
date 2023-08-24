class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
       
        def countOnesBits(num):
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count
        
        def isPrime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True

            if num % 2 == 0 or num % 3 == 0:
                return False

            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6

            return True
        
        result = 0
        for num in range(left,right+1):
            count_num = countOnesBits(num)
            if isPrime(count_num):
                result += 1
        return result