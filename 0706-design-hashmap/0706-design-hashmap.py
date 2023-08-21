class MyHashMap(object):

    def __init__(self):
        # Initialize your data structure here.
        self.size = 1000  # Choose a size for the underlying array
        self.array = [None] * self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        if self.array[index] is None:
            self.array[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.array[index]):
                if existing_key == key:
                    self.array[index][i] = (key, value)
                    break
            else:
                self.array[index].append((key, value))

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.size
        slot = self.array[index]
        if slot is not None:
            for existing_key, value in slot:
                if existing_key == key:
                    return value
        return -1  # Key not found

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size
        slot = self.array[index]
        if slot is not None:
            for i, (existing_key, value) in enumerate(slot):
                if existing_key == key:
                    del slot[i]
                    break

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)