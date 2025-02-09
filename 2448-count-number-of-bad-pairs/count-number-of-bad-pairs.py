class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n - 1))//2

        pairs = defaultdict(int)
        good_pairs = 0
        for i in range(n):
            diff = nums[i] - i
            good_pairs += pairs[diff]
            pairs[diff] += 1
        return total - good_pairs
            