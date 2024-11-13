class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def countLess(val: int) -> int:
            result = 0
            j = len(nums) - 1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                result += max(0, j-i)
            return result
        nums.sort()
        return countLess(upper) - countLess(lower - 1)
            