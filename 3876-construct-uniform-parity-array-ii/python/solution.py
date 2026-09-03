class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')
        minEven = float('inf')

        for n in nums1:
            if n%2:
                minOdd=min(minOdd,n)
            else:
                minEven=min(minEven,n)
        if minOdd==float('inf') or minEven==float('inf'):
            return True
        return minOdd<minEven

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')
        minEven = float('inf')

        for n in nums1:
            if n&1:
                minOdd=min(minOdd,n)
            else:
                minEven=min(minEven,n)
        if minOdd==float('inf') or minEven==float('inf'):
            return True
        return minOdd<minEven