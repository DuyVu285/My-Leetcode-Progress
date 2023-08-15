class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cur, res = 0,0,0
        for n in nums:
            cur = cur + 1 if prev < n else 1
            res = max(cur, res)
            prev = n
        
        return res
            