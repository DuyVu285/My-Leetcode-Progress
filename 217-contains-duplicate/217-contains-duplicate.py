class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp = nums
        if len(set(temp)) != len(nums):
            return True
        return False