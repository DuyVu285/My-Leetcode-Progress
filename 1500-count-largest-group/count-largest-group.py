class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        for i in range(1, n + 1):
            index = self.sum_to_one_digit(i)
            groups[index] += 1
        max_val = max(groups.values())
        count = sum(1 for v in groups.values() if v == max_val)
        return count

    def sum_to_one_digit(self, n) -> int:
        return sum(int(d) for d in str(n))
