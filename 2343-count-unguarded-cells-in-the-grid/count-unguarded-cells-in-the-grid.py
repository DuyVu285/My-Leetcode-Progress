class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i,j in walls:
            dp[i][j] = 2
        
        for guard_i, guard_j in guards:
            dp[guard_i][guard_j] = 1

        for guard_i, guard_j in guards:
            for row in range(guard_i-1, -1, -1):
                if dp[row][guard_j] == 2 or dp[row][guard_j] == 1:
                    break
                dp[row][guard_j] = -1

            for row in range(guard_i+1, m):
                if dp[row][guard_j] == 2 or dp[row][guard_j] == 1:
                    break
                dp[row][guard_j] = -1

            for col in range(guard_j+1, n):
                if dp[guard_i][col] == 2 or dp[guard_i][col] == 1:
                    break
                dp[guard_i][col] = -1
           
            for col in range(guard_j-1, -1, -1):
                if dp[guard_i][col] == 2 or dp[guard_i][col] == 1:
                    break
                dp[guard_i][col] = -1
        
        unguarded = sum(row.count(0) for row in dp)
        return unguarded
