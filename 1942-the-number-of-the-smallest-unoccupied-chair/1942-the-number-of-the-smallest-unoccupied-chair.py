class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        sorted_times = sorted(enumerate(times), key=lambda x: x[1][0])  # Sort by arrival time
    
        # Min-heap to track the available chairs
        available_chairs = []
        for i in range(n):
            heapq.heappush(available_chairs, i)  # Initially, all chairs from 0 to n-1 are available

        # Min-heap to track the leaving events (leaving time, chair number)
        occupied_chairs = []  # (leaving_time, chair_number)
    
        # Process each friend's arrival and departure
        for idx, (arrival, leaving) in sorted_times:
            # First, free any chairs where the friend has already left by this arrival time
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                leave_time, chair_number = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair_number)
        
        # Assign the smallest available chair
            chair = heapq.heappop(available_chairs)
        
        # If this is the target friend, return the chair number
            if idx == targetFriend:
                return chair
        
        # Add this friend's leaving event to the occupied chairs heap
            heapq.heappush(occupied_chairs, (leaving, chair))   