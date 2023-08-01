class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique = set(candyType)
        n = len(candyType)/2
        if len(unique) >= n:
            return n
        else:
            return len(unique)