class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        if n>=10**3:
            res+=n - (10**3 - 1)
        if n>=10**6:
            res+=n - (10**6 - 1)
        if n>=10**9:
            res+=n - (10**9 - 1)
        if n>=10**12:
            res+=n - (10**12 - 1)
        if n>=10**15:
            res+=n - (10**15 - 1)
        return res


class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        for i in range(3,16,3):
            if n>=10**i:
                res+= n - ((10**i) -1)
        return res