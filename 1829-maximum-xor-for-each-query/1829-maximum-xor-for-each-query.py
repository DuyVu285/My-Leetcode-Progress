class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxXOR, arrayXOR, ans = (1 << maximumBit) - 1, reduce(ixor, nums), []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(arrayXOR ^ maxXOR)
            arrayXOR ^= nums[i]
        return ans