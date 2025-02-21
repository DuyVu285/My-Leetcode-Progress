class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums[1:])
        for i in range(len(nums)-1):
            if sum_left == sum_right:
                return i 
            sum_left += nums[i]
            sum_right -= nums[i+1]
        if sum_left == sum_right:
            return len(nums) - 1
        return -1