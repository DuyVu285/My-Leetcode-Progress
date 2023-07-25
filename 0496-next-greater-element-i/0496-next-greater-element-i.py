class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for num1 in nums1:
            index_in_nums2 = nums2.index(num1)
            nextbig = []
            for i in range(index_in_nums2 + 1, len(nums2)):
                if nums2[i] > num1:
                    nextbig.append(nums2[i])
                    break
            if nextbig:
                result.append(max(nextbig))
            else:
                result.append(-1)
        return result