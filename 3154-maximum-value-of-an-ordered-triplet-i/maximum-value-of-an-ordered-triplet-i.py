class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxElement = 0
        maxDifference = 0
        maxTripletValue = 0
        for i in range(len(nums)):
            maxTripletValue = max(maxTripletValue, maxDifference*nums[i])
            maxDifference = max(maxDifference, maxElement - nums[i])
            maxElement = max(maxElement, nums[i])
        return maxTripletValue