class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = 0
        n = len(nums)

        for i in range(n):
            missing ^= i ^ nums[i]

        missing ^= n

        return missing