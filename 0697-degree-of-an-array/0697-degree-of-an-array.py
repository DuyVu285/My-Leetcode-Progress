class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index = {}
        frequency = {}
        right_index = {}

        for i, num in enumerate(nums):
            if num not in frequency:
                frequency[num] = 0
                left_index[num] = i
            frequency[num] += 1
            right_index[num] = i

        degree = max(frequency.values())
        min_length = float('inf')

        for num in frequency:
            if frequency[num] == degree:
                length = right_index[num] - left_index[num] + 1
                min_length = min(min_length, length)

        return min_length