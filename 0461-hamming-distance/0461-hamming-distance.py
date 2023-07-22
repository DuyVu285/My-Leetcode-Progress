class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        max_length = max(len(x_bin), len(y_bin))
        x_bin = x_bin.zfill(max_length)
        y_bin = y_bin.zfill(max_length)

        hamming_distance = sum(bit_x != bit_y for bit_x, bit_y in zip(x_bin, y_bin))

        return hamming_distance