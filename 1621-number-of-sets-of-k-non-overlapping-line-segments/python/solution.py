class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7 
        total = n+k-1
        choose = 2*k
        def factorial(x):
            res = 1
            for i in range(2,x+1):
                res = (res*i)%MOD
            return res
        
        a = factorial(total)
        b = factorial(choose)
        c = factorial(total-choose)

        return (a * pow(b,MOD-2,MOD)*pow(c,MOD-2,MOD) )%MOD