class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                perimeter += 4*grid[i][j]
                if i > 0: perimeter -= grid[i][j]*grid[i-1][j]
                if i < m - 1: perimeter -= grid[i][j]*grid[i+1][j]
                if j > 0: perimeter -= grid[i][j]*grid[i][j-1]
                if j < n - 1: perimeter -= grid[i][j]*grid[i][j+1]
        return perimeter