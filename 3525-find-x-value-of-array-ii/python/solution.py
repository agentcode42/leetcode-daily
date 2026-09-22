class SegTree:
    def __init__ (self,nums,k):
        self.n = len(nums)
        self.k = k
        self.tree_product = [1]*(4*self.n)
        self.tree_reminder = [[0]*self.k for _ in range(4*self.n)]
        if self.n>0:
            self.build(0,0,self.n -1 ,nums)
    def merge(self,left,right):
        res  = list(left[1])
        for i in range(self.k):
            curr_rem = (left[0]*i)%self.k
            res[curr_rem]+=right[1][i]
        return ((left[0]*right[0])%self.k,res)
    
    def build(self,node,l,r,nums):
        if l==r:
            val = nums[l]%self.k
            self.tree_product[node]=val
            self.tree_reminder[node][val]=1
            return (self.tree_product[node],self.tree_reminder[node])
        
        if l<r:
            mid = (l+r)//2
            left = self.build(2*node+1,l,mid,nums)
            right = self.build(2*node+2,mid+1,r,nums)
            prod,rem = self.merge(left,right)
            self.tree_product[node]=prod
            self.tree_reminder[node]=rem
            return (prod,rem)

    def update(self,node,l,r,idx,val):
        if l==r:
            val = val%self.k
            self.tree_product[node]=val
            self.tree_reminder[node]=[0]*self.k
            self.tree_reminder[node][val]=1
            return 
        if l<r:
            mid = (l+r)//2
            if idx<=mid:
                self.update(2*node+1,l,mid,idx,val)
            else:
                self.update(2*node+2,mid+1,r,idx,val)
            
            prod,rem = self.merge(
                (self.tree_product[2*node+1],self.tree_reminder[2*node+1]),
                (self.tree_product[2*node+2],self.tree_reminder[2*node+2]))
            self.tree_product[node]=prod
            self.tree_reminder[node]=rem

    def query(self,node,l,r,start,end):
        if start<=l and r<=end:
            return (self.tree_product[node],self.tree_reminder[node])
        if r<start or l>end:
            return (1,[0]*self.k)
        
        else:
            mid = (l+r)//2
            left = self.query(2*node+1,l,mid,start,end)    
            right = self.query(2*node+2,mid+1,r,start,end)
            return self.merge(left,right)    
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = SegTree(nums,k)
        res = []
        for idx,val,start,x in queries:
            seg.update(0,0,n-1,idx,val)
            _ , rem = seg.query(0,0,n-1,start,n-1)
            res.append(rem[x])
        return res



'''
Brute Force solution that do not work
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        res = []
        for index,value,start,x in queries:
            nums[index]=value
            rems = [0]*k
            curr = 1
            for i in range(start,n):
                curr = (curr*nums[i])%k
                rems[curr]+=1
            res.append(rems[x])
        return res
'''