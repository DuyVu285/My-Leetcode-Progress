class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        i = 0
        while i < n - 1:
            i += bits[i] + 1  # Skip one or two bits based on the value at i
        
        # If we are at the last bit, it's a valid one-bit character
        return i == n - 1