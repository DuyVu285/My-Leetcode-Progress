class Solution:
    def minChanges(self, s: str) -> int:
        current_char = s[0]
        consecutive_count = 0
        minChanges = 0
        for i in range(len(s)):
            if current_char == s[i]:
                consecutive_count += 1
                continue
            if consecutive_count % 2 == 0:
                consecutive_count = 1
                current_char = s[i]
            else:
                consecutive_count = 0
                minChanges += 1
            
        return minChanges
        