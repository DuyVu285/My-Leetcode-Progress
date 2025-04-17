class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        store = defaultdict(list)
        count = 0
        for i, num in enumerate(nums):
            if num in store:
                for num_idx in store[num]:
                    if (i*num_idx) % k == 0:
                        count += 1
            store[num].append(i)
        return count 