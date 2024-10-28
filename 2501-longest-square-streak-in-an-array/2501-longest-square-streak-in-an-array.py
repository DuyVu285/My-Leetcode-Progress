class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        max_streak = -1
        
        for num in nums:
            streak_length = 0
            current = num
            
            while current in nums_set:
                streak_length += 1
                current = current ** 2
                
            if streak_length >= 2:
                max_streak = max(max_streak, streak_length)
        return max_streak