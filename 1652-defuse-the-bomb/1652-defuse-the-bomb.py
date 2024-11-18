class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted = [0] * n
        if k > 0:
            for i in range(n):
                j = i+1
                element_sum = 0
                for j in range(1,k+1):
                    element_sum += code[(i + j) % n]
                decrypted[i] = element_sum
        elif k < 0:
            for i in range(len(code)):
                j = i-1
                element_sum = 0
                for j in range(1, abs(k) + 1):
                    element_sum += code[(i-j)%n]
                decrypted[i] = element_sum
        else:
            decrypted = [0] * n
        return decrypted