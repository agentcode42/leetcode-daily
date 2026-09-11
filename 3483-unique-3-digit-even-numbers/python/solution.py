class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        res = 0
        for n in range(100,1000,2):
            a = n%10
            b = (n//10)%10
            c = n//100

            if count[a]>0:
                count[a]-=1
                if count[b]>0:
                    count[b]-=1
                    if count[c]>0:
                        res+=1
                    count[b]+=1
                count[a]+=1
        return res