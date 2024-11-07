class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bit_length = max(candidates).bit_length()
        max_count = 0

        # Iterate over each bit position
        for bit_position in range(max_bit_length):
            count = 0
            for num in candidates:
                # Check if the current bit is set in num
                if num & (1 << bit_position):
                    count += 1
            # Update max_count if this bit position has more 1s
            max_count = max(max_count, count)

        return max_count