class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left, right = 0, k - 1
        window_sum = sum(nums[:k])
        max_average = window_sum / float(k)

        while right < len(nums) - 1:
            right += 1
            window_sum += nums[right] - nums[left]
            left += 1
            max_average = max(max_average, window_sum / float(k))

        return max_average