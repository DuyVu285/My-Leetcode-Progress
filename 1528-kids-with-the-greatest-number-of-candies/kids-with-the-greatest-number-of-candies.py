class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        greatest = max(candies)
        n = len(candies)
        for i in range(n):
            if candies[i] + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result