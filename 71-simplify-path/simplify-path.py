class Solution:
    def simplifyPath(self, path: str) -> str:
        path_formatted = path.split("/")
        stack = []
        for char in path_formatted:
            if stack and char == "..":
                stack.pop()
            elif char not in [".","",".."]:
                stack.append(char)
        return "/" + "/".join(stack)