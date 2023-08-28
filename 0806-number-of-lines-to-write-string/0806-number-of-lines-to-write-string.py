class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1  # Initialize the number of lines to 1
        line_width = 0  # Initialize the current line's width

        for char in s:
            char_width = widths[ord(char) - ord('a')]  # Get the width of the character
            if line_width + char_width > 100:
                lines += 1
                line_width = char_width
            else:
                line_width += char_width

        return [lines, line_width]