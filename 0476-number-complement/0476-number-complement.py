class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        number_binary = bin(num)[2:]
        complement = ''.join('1' if bit == '0' else '0' for bit in number_binary)
        return int(complement, 2)