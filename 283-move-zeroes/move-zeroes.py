class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
                else:
                    right += 1
            else:
                left = right
                right += 1