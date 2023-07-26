class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)
        result = ""

        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num //= 7

        if is_negative:
            result = "-" + result

        return result