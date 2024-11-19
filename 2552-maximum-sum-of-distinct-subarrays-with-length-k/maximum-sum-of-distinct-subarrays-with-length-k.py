class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        max_sum = 0
        current_sum = 0
        freq = {}

        left = 0

        for right in range(n):
            current_sum += nums[right]
            freq[nums[right]]= freq.get(nums[right],0)+1

            if right-left+1 > k:
                current_sum -= nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            
            if right-left+1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
            







           