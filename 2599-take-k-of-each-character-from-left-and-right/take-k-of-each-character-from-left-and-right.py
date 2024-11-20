class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total_count = Counter(s)
        if total_count['a'] < k or total_count['b'] < k or total_count['c'] < k:
            return -1
        
        n = len(s)
        left = 0
        window_count = Counter()
        max_window_size = 0
        
        for right in range(n):
            window_count[s[right]] += 1
            
            while (total_count['a'] - window_count['a'] < k or
                total_count['b'] - window_count['b'] < k or
                total_count['c'] - window_count['c'] < k):
                window_count[s[left]] -= 1
                left += 1
            
            max_window_size = max(max_window_size, right - left + 1)
        
        return n - max_window_size