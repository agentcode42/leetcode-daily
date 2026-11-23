class ProductOfNumbers:

    def __init__(self):
        self.product_nums = [1]
        self.length = 0

    def add(self, num: int) -> None:
        if num!=0:
            self.product_nums.append(self.product_nums[-1]*num)
            self.length+=1
        else:
            self.product_nums=[1]
            self.length = 0
    def getProduct(self, k: int) -> int:
        if k>self.length:
            return 0
        return self.product_nums[-1]//self.product_nums[-(k+1)]












# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)