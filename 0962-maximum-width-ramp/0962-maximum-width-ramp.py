class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        if n <= 1:
            return 0
        
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        maxRamp = 0
        
        for j in reversed(range(n)):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                maxRamp = max(maxRamp, j - i)
        
        return maxRamp
            
                