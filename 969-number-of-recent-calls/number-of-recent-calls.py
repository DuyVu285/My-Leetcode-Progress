class RecentCounter:

    def __init__(self):
        self.recent = deque()
    def ping(self, t: int) -> int:
        count = 1
        for previous_t in self.recent:
            if t - 3000 <= previous_t:
                count += 1
        self.recent.append(t)
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)