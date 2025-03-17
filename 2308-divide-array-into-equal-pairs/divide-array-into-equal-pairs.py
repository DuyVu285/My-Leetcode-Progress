class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for item, count in freq.items():
            if (count & 1):
                return False
        return True