class MyHashSet(object):

    def __init__(self):
        self.key_range = 769  # A prime number for better distribution
        self.buckets = [None] * self.key_range

    def _hash(self, key):
        return key % self.key_range

    def _get_bucket(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        return self.buckets[index]

    def add(self, key):
        bucket = self._get_bucket(key)
        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        bucket = self._get_bucket(key)
        if key in bucket:
            bucket.remove(key)

    def contains(self, key):
        bucket = self._get_bucket(key)
        return key in bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)