class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        if 999<n<1000000:
            return n-999