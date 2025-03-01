class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0

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
        
        return nums