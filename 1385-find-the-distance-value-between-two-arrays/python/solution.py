class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for a in arr1:
            flag = True
            for b in arr2:
                if abs(a-b)<=d:
                    flag=False
                    break
            if flag:res+=1
        return res