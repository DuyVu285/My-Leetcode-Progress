class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        maxVolume = 0
        while left < right:
            volume = min(height[right],height[left]) * (right-left)
            maxVolume = max(maxVolume, volume)
            
            if height[left] <  height[right]:
                left += 1
            else:
                right -= 1
        return maxVolume