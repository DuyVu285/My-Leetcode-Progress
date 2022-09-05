class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = x
        reverse = 0
        while number > 0:
            reminder = number%10
            reverse = reverse*10 + reminder
            number = number/10
        print(reverse)
        if (x == reverse):
            return True
        else:
            return False