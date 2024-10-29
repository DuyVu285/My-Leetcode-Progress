class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(row,col):
            if col == n - 1:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            
            max_moves = 0
            directions = [(1,1), (0,1),(-1,1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_moves = max(max_moves,1 + dfs(new_row, new_col))
            
            dp[row][col] = max_moves
            return dp[row][col]
        
        max_moves_result = 0
        for row in range(m):
            max_moves_result = max(max_moves_result, dfs(row,0))
        return max_moves_result
            