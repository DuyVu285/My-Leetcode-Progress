class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.recursion(nums, [],result)
        return result
    
    def recursion(self, nums: List[int], path: List[int],result: List[List[int]]):
        if not nums:
            result.append(path)
            return result
        for i in range(len(nums)):
            self.recursion(nums[:i] + nums[i+1:], path + [nums[i]], result)