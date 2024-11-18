class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted = [0] * n

        if k == 0:
            return decrypted

        if k > 0:
            current_sum = sum(code[1 : k + 1])
            for i in range(n):
                decrypted[i] = current_sum
                current_sum -= code[(i + 1) % n]
                current_sum += code[(i + k + 1) % n]
        if k < 0:
            k = -k
            current_sum = sum(code[-k:])
            for i in range(n):
                decrypted[i] = current_sum
                current_sum -= code[(i - k) % n]
                current_sum += code[i % n]

        return decrypted
