class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        max_arrows = 1
        points.sort(key=lambda x: x[1])

        current_end = points[0][1]

        for start, end in points[1:]:
            if start > current_end:
                max_arrows += 1
                current_end = end
                
        return max_arrows