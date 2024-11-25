class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if not nums:
            return []
    
        ans = []
        start = nums[0]
        for i in range(1, n):
            if nums[i] != nums[i-1]+1:
                ans.append(f"{start}" if start == nums[i-1] else f"{start}->{nums[i-1]}")
                start = nums[i]
        ans.append(f"{start}" if start == nums[-1] else f"{start}->{nums[-1]}")
        return ans

            