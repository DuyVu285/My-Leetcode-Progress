class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
            
        directions = [(1,0), (0,1),(-1,0),(0,-1)]

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        heap = [(0, 0, 0)]
        visited = [[False] * n for _ in range(m)]

        while heap:
            time, x, y = heapq.heappop(heap)

            if (x, y) == (m-1, n-1):
                return time

            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if  0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] <= time + 1:
                        heapq.heappush(heap, (time + 1, nx, ny))
                    else:
                        diff = grid[nx][ny] - time
                        if diff % 2 == 1:
                            heapq.heappush(heap, (grid[nx][ny], nx, ny))
                        else:
                            heapq.heappush(heap, (grid[nx][ny]+1, nx, ny))                   
        return -1


