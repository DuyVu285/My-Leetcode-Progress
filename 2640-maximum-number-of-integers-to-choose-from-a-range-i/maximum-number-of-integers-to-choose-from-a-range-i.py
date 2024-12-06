class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = {x for x in banned if x <= n}
        count = 0
        current_sum = 0
        for i in range(1,n+1):
            if i not in banned_set:
                if current_sum + i <= maxSum:
                    current_sum += i
                    count += 1
                else:
                    break
        return count



