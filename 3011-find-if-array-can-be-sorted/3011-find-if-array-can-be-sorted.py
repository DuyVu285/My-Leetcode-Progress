class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max, new_max = 0 , nums[0]
        bitcount = bin(nums[0]).count('1')
        for num in nums[1:]:
            if num < prev_max:
                return False
            if bitcount == bin(num).count('1'):
                new_max = max(new_max, num)
            else:
                prev_max = new_max
                if num < prev_max:
                    return False
                bitcount = bin(num).count('1')
                new_max = num
        
        return True
        