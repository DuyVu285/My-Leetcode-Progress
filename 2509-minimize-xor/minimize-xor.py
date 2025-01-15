class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits_num2 = bin(num2).count('1')

        x = 0
        for i in range(31, -1, -1):
            if set_bits_num2 > 0 and (num1 & (1 << i)):
                x |= (1 << i)
                set_bits_num2 -= 1
    
        for i in range(32):
            if set_bits_num2 > 0 and not (x & (1 << i)):
                x |= (1 << i)
                set_bits_num2 -= 1
        
        return x