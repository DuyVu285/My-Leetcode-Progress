class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key = lambda x: x[0])
        merged = [intervals[0]]

        for current_start, current_end in intervals[1:]:
            last_start, last_end = merged[-1]

            if current_start <= last_end:
                merged[-1] = [last_start, max(last_end, current_end)]
            else:
                merged.append([current_start, current_end])

        return merged
