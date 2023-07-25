class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """                
        if not timeSeries:
            return 0

        total_duration = 0
        for i in range(1, len(timeSeries)):
            total_duration += min(timeSeries[i] - timeSeries[i-1], duration)

        # Add the duration of the last attack
        total_duration += duration

        return total_duration
                