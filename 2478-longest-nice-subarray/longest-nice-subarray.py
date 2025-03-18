class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        curr_bits = 0 
        max_length = 1 

        for right in range(len(nums)):
            while (curr_bits & nums[right]) != 0:
                curr_bits ^= nums[left]  
                left += 1 

            curr_bits |= nums[right]
            max_length = max(max_length, right - left + 1) 

        return max_length
