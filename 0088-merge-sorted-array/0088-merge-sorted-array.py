class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = m + n 
        while m < length:
            nums1[m] = nums2[n-1]
            m += 1
            n -= 1
            
        nums1.sort()
        return nums1