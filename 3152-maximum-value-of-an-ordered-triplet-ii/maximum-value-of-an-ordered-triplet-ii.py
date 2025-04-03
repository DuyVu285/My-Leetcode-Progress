class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxElement = 0
        maxDifferent = 0
        maxTripletValue = 0 
        for i in range(n):
            maxTripletValue = max(maxTripletValue, maxDifferent*nums[i])
            maxDifferent = max(maxDifferent, maxElement - nums[i])
            maxElement = max(maxElement, nums[i])
        return maxTripletValue