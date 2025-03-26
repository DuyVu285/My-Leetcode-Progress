class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        if not grid or not grid[0]:
            return -1

        flattened = [num for row in grid for num in row]
        flattened.sort()

        if len(set(flattened)) == 1:
            return 0

        base = flattened[0]
        for num in flattened:
            if (num - base) % x != 0:
                return -1

        middle = flattened[len(flattened) // 2]
        count = sum([abs(num - middle) // x for num in flattened])
        return count 
