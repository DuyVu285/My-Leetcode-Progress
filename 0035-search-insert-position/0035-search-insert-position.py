class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target:
                index += 1
                
        return index