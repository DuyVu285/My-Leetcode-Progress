class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 1
        n = len(nums)
        longest = 1
        while end < n:
            if nums[end] > nums[end-1]:
                longest = max(longest, end-start+1)
                end += 1
            else:
                start = end
                end += 1

        start = 0
        end = 1
        while end < n:
            if nums[end] < nums[end-1]:
                longest = max(longest, end-start+1)
                end +=1
            else:
                start = end
                end += 1

        return longest

