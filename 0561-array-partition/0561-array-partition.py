class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum
        