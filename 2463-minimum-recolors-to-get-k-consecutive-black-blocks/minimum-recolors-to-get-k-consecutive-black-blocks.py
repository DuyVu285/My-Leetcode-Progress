class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = blocks[:k].count('W')
        current_operations = min_operations

        # Sliding window across the rest of the string
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_operations -= 1  # Remove the leftmost character
            if blocks[i] == 'W':
                current_operations += 1  # Add the new rightmost character
            
            min_operations = min(min_operations, current_operations)

            # If we ever reach zero, we can stop early (optimal case)
            if min_operations == 0:
                return 0
        
        return min_operations