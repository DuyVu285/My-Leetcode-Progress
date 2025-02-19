class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a','b','c']
        result = []
        self.generateHappyStrings(letters, "", result, n)
        if k > len(result):
            return ""
        return result[k-1]

    def generateHappyStrings(self, letters: List[str], path: str, result: List[str], n: int):
        if len(path) == n:
            result.append(path)
            return

        for i in range(len(letters)):
            if not path or path[-1] != letters[i]:
                self.generateHappyStrings(letters, path + letters[i], result, n)
