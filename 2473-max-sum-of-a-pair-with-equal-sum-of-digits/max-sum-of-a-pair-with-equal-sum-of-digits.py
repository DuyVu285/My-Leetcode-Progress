class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_digits = defaultdict(list)
        max_sum = -1
        for num in nums:
            sum_digit = sum(map(int, str(num)))
            sum_digits[sum_digit].append(num)
        for values in sum_digits.values():
            if len(values) >= 2:
                total_sum = sum(sorted(values)[-2:])
                max_sum = max(max_sum, total_sum)
        return max_sum

        