class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def merge_intervals(intervals):
            intervals.sort()
            merged = []
            for start, end in intervals:
                if merged and start < merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], end)
                else:
                    merged.append([start, end])
            return len(merged)

        x_intervals = [[rect[0], rect[2]] for rect in rectangles]
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]

        return merge_intervals(x_intervals) > 2 or merge_intervals(y_intervals) > 2
