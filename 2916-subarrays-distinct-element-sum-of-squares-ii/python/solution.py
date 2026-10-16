class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9+7
        n = len(nums)

        sum_counts =[0]*(4*n)
        sum_squares =[0]*(4*n)
        lasy_updates =[0]*(4*n)

        def update(node_idx,length,inc):
            sum_squares[node_idx]+=2*inc*sum_counts[node_idx] + length*(inc**2)
            sum_counts[node_idx]+= inc*length
            lasy_updates[node_idx]+=inc
        
        def update_range(node_idx,node_left,node_right,query_left,query_right):
            if query_left<=node_left and node_right<=query_right:
                update(node_idx,node_right-node_left+1,1)
                return 
            mid  = (node_left+node_right)//2

            if lasy_updates[node_idx]:
                update(2*node_idx,mid-node_left+1,lasy_updates[node_idx])
                update(2*node_idx+1,node_right-mid,lasy_updates[node_idx])
                lasy_updates[node_idx]=0

            if query_left<=mid:
                update_range(2*node_idx,node_left,mid,query_left,query_right)
            if query_right>mid:
                update_range(2*node_idx+1,mid+1,node_right,query_left,query_right)

            sum_counts[node_idx] = sum_counts[2*node_idx]+ sum_counts[2*node_idx+1]
            sum_squares[node_idx] =sum_squares[2*node_idx] +sum_squares[2*node_idx+1]

        last_seen = {}
        total= 0
        for i, num in enumerate(nums):
            range_left = last_seen.get(num,-1)+1
            update_range(1,0,n-1,range_left,i)
            last_seen[num]=i
            total = (total+sum_squares[1])%MOD
        return total













