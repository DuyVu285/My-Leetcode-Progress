class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        return self.recursion(nums, count)
    
    def recursion(self, nums: List[int], count: int) -> int:
        n = len(nums)
        if len(set(nums)) != n:
            count += 1
            return self.recursion(nums[3:], count)
        return count