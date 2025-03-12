class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positiveCount = len(nums) - self.upperBound(nums)
        negativeCount = self.lowerBound(nums)
        return max(positiveCount, negativeCount)
        
    def lowerBound(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < 0:
                start = mid + 1
            else:
                end = mid -1
                index = mid

        return index
    
    def upperBound(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        index = len(nums)

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= 0:
                start = mid + 1
            else:
                end = mid -1
                index = mid

        return index