class NumberContainers:

    def __init__(self):
        self.pair1 = {}
        self.pair2 = {}

    def change(self, index: int, number: int) -> None:
        if index in self.pair1:
            old_number = self.pair1[index]
            self.pair2[old_number].discard(index)
            if not self.pair2[old_number]:
                del self.pair2[old_number]
        
        self.pair1[index] = number
        if number not in self.pair2:
            self.pair2[number] = SortedSet()
        self.pair2[number].add(index)

    def find(self, number: int) -> int:
        if number in self.pair2 and self.pair2[number]:
            return self.pair2[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)