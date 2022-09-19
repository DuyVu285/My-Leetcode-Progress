class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = 0
        unique_list = set(nums)
        for x in unique_list:
            if nums.count(x) > (len(nums)/2) and nums.count(x) >= majority:
                majority = x
        return majority