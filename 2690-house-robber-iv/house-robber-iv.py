class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)
        total_houses = len(nums)

        while left < right:
            mid = (left + right) // 2
            housesRobbed = 0

            index = 0
            while index < total_houses:
                if nums[index] <= mid:
                    housesRobbed += 1
                    index += 2
                else:
                    index += 1
            
            if housesRobbed >= k:
                right = mid
            else:
                left = mid + 1
        
        return left