class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        if len(s) <= 1:
            return False
        
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif stack and pairs[stack[-1]] == bracket:
                stack.pop()
            else:
                return False
        
        return not stack