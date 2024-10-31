import random

class RandomizedSet:

    def __init__(self):
        self.result = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.result.append(val)
        self.dict[val] = len(self.result) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        index = self.dict[val]
        last_element = self.result[-1]
        
        self.result[index] = last_element
        self.dict[last_element] = index
        
        self.result.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.result)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()