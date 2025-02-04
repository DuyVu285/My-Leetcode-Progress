class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        start = 0
        end = 1
        n = len(nums)
        current_sum = nums[start]
        max_sum = current_sum

        while end < n:
            if nums[end-1] < nums[end]:
                current_sum += nums[end]
            else:
                max_sum = max(max_sum, current_sum)
                start = end
                current_sum = nums[start]
            end += 1
        max_sum = max(max_sum, current_sum)
        return max_sum