class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauty = []
        current_max = 0
        ans = []
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        for query in queries:
            idx = bisect.bisect_right(max_beauty, (query, float('inf'))) - 1
            if idx >= 0:
                ans.append(max_beauty[idx][1])
            else:
                ans.append(0)
        
        return ans
                    
                