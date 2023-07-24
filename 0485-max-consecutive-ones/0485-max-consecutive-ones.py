class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        current = 0
        
        for num in nums:
            if num == 1:
                current += 1
                count = max(count, current)
            else:
                current = 0
                
        return count
            
            