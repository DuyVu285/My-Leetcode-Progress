class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = nums1 + nums2
        array.sort()
        
        n = len(array)
        if n % 2 == 1:
            median = array[n // 2]
        else:
            median = (array[n // 2 - 1] + array[n // 2]) / 2.0
        return median