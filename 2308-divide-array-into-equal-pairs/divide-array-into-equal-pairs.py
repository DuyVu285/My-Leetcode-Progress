class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for item, count in freq.items():
            if not (count & 1) == 0:
                return False
        return True