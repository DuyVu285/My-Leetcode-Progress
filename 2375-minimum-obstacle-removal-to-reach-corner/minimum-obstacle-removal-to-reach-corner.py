class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        target = (m-1,n-1)
        start = (0,0)

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        queue = deque([(0,start)])
        visited = set()
        visited.add(start)

        while queue:
            removed, (x,y) = queue.popleft()

            if (x,y) == target:
                return removed
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx,ny))
                    if grid[nx][ny] == 1:
                        queue.append((removed + 1, (nx, ny)))
                    else:
                        queue.appendleft((removed, (nx, ny)))

        return 0
