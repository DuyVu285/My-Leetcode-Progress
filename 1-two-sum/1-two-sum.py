class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx,x in enumerate(nums):
            for idy,y in enumerate(nums):
                if idx != idy:
                    if x + y == target:
                        return idx,idy
                    
        
                    