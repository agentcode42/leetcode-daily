class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            temp = []
            for i in range(0,len(s),k):
                group = s[i:i+k]
                digit_sum = sum(int(n) for n in group)
                temp.append(str(digit_sum))
            s = "".join(temp)
        return s