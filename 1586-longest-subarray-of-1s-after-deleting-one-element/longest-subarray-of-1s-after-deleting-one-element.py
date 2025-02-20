class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        count = 0
        current_max = 0
        last_index = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                count += 1
                if count == 2:
                    start = last_index + 1
                    count -= 1
                last_index = end
            current_max = max(current_max, end - start)
        return current_max