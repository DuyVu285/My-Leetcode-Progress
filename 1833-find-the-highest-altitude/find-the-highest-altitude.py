class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_altitude = 0
        current_max = 0
        for i in range(len(gain)):
            prefix_altitude += gain[i]
            current_max = max(current_max, prefix_altitude)
        return current_max