class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = [[i + 1] for i in range(n)]
        
        def bfs():
            queue = deque([(0, 0)])
            visited = set()
            visited.add(0)
            
            while queue:
                current, distance = queue.popleft()
                
                if current == n - 1:
                    return distance
                
                for neighbor in adj_list[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
                        visited.add(neighbor)
        
        result = []
        for src, dst in queries:
            adj_list[src].append(dst)
            result.append(bfs())
        
        return result
                

