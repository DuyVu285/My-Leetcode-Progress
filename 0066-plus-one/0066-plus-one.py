class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = 1

        for i in range(length - 1, -1, -1):
            digits[i] += carry

            if digits[i] < 10:
                return digits

            digits[i] = 0

        digits.insert(0, 1)
        return digits   