class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)

        def check(step):
            for i in range(1,n):
                prev = (zero + (i-1)*step)%n
                curr = (zero+i*step)%n

                if nums[prev]>nums[curr]:
                    return False
            return True
        inc = check(1)
        dec = check(-1)
        if not inc and not dec:
            return -1
        if inc:
            return min(zero,n-zero+2)
        else:
            return min(zero+2,n-zero)