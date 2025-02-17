class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []
        self.recursion(tiles,"", result)
        return len(result)
    
    def recursion(self, tiles: str, path: str, result: List[str]):
        if path and path not in result:
            result.append(path)
        if not tiles:
            return result
        for i in range(len(tiles)):
            self.recursion(tiles[:i]+tiles[i+1:], path + tiles[i], result)