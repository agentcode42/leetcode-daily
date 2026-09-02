# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
            prev_c = -1
            start_c = -1
            min_c = float('inf')
            
            prev = curr = head
            i = 0
            while curr.next:
                nexts= curr.next
            
                if prev.val<curr.val>nexts.val or prev.val>curr.val<nexts.val:
                    if start_c == -1:
                        start_c = i
                    if prev_c!=-1:
                        min_c = min(min_c,i-prev_c)
                    prev_c = i
                prev = curr
                curr = curr.next
                i+=1

            if min_c==float('inf'):
                return [-1,-1]
            return [min_c,prev_c-start_c]
        
        
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
            nums = []
            curr = head
            while curr:
                nums.append(curr.val)
                curr = curr.next
            
            prev_c = -1
            start_c = -1
            min_c = len(nums)
            if len(nums)<4:
                return [-1,-1]
            for i in range(1,len(nums)-1):
                if nums[i-1]<nums[i]>nums[i+1] or nums[i-1]>nums[i]<nums[i+1] :
                    if start_c == -1:
                        start_c = i
                    if prev_c!=-1:
                        min_c = min(min_c,i-prev_c)
                    prev_c = i
            
            if min_c==len(nums):
                return [-1,-1]
            return [min_c,prev_c-start_c]