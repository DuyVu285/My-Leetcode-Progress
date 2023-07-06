class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self._top = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        self._top = x
        
    def pop(self):
        """
        :rtype: int
        """
        while(len(self.queue1) > 1):
            self._top = self.queue1.popleft()
            self.queue2.append(self._top)
        result = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self):
        """
        :rtype: int
        """
        return self._top
        
    
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()