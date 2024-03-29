class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        a = sum(nums)
        b = sum(set(nums))
        c = (n*(n+1))//2
        
        return [a-b,c-b]