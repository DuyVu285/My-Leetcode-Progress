class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_each = {}
        color = {}
        result = []

        for ball, current_color in queries:
            if ball in color_each:
                prev_color = color_each[ball]
                color[prev_color] -= 1
                if color[prev_color] == 0:
                    del color[prev_color]
            color_each[ball] = current_color
            color[current_color] = color.get(current_color, 0) + 1
            result.append(len(color))
        return result