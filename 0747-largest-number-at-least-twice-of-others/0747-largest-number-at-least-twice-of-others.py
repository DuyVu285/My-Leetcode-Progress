class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_index = -1
        largest_val = -1
        second_largest_val = -1

        # Find the largest element and its index
        for i, num in enumerate(nums):
            if num > largest_val:
                second_largest_val = largest_val
                largest_val = num
                largest_index = i
            elif num > second_largest_val:
                second_largest_val = num

        # Check if the condition holds
        if largest_val >= 2 * second_largest_val:
            return largest_index
        else:
            return -1