class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit_sum = carry

            if i >= 0:
                digit_sum += int(num1[i])
                i -= 1

            if j >= 0:
                digit_sum += int(num2[j])
                j -= 1

            result.append(str(digit_sum % 10))
            carry = digit_sum // 10

        return ''.join(result[::-1])