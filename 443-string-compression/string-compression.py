class Solution:
    def compress(self, chars: List[str]) -> int:
        start, end = 0, 0
        while end < len(chars):
            char = chars[end]
            count = 0
            while end < len(chars)and char == chars[end]:
                end += 1
                count += 1
            chars[start] = char
            start += 1
            if count > 1:
                for digit in str(count):
                    chars[start] = digit
                    start += 1
        return start
