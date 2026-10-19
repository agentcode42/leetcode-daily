class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count_less = 0
        count_target = 0
        for n in nums:
            if n<target:
                count_less+=1
            elif n== target:
                count_target+=1
        res = []
        for i in range(count_target):
            res.append(count_less+i)
        return res