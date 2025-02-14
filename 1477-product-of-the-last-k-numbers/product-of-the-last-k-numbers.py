class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = []
        self.product = 1
    def add(self, num: int) -> None:
        if num is not 0:
            self.product *= num
            self.prefix_product.append(self.product)
        else:
            self.product = 1
            self.prefix_product = []
    def getProduct(self, k: int) -> int:
        if k == len(self.prefix_product):
            return self.prefix_product[-1]
        elif k > len(self.prefix_product):
            return 0
        else:
            return int(self.prefix_product[-1]/self.prefix_product[-1-k])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)