class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char is "*" and stack:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)