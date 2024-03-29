class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(x1, y1, x2, y2, x3, y3):
            return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        
        n = len(points)
        max_area = 0.0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    max_area = max(max_area, area(x1, y1, x2, y2, x3, y3))

        return max_area