class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while n != 1:
            if n in track:
                return False
            track.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return True
