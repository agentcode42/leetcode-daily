class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        total = sum
        if num*9<total:
            return ""
        digit_9 = total//9
        remain = num - digit_9
        total = total-(digit_9*9)
        if remain==0:
            return "9"*digit_9
        res = "9"*digit_9 + str(total) + "0"*(remain-1)
        return res