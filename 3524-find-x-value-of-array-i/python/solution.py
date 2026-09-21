class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0]*k
        reminders = [0]*k
        for n in nums:
            new_r = [0]*k
            new_r[n%k]=1
            for i in range(k):
                curr = (n*i)%k
                new_r[curr]+=reminders[i]
            for i in range(k):
                res[i] +=new_r[i]
            reminders = new_r
        return res