class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        curr_tree = defaultdict(list)
        for i in range(1,n):
            curr_tree[parent[i]].append(i)
        
        prev = [-1]*26
        def dfs(node):
            c = ord(s[node])-ord('a')
            old = prev[c]
            if old !=-1:
                parent[node]=old
            prev[c]=node
            for child in curr_tree[node]:
                dfs(child)
            prev[c]=old
        
        dfs(0)
        new_tree = defaultdict(list)
        for i in range(1,n):
            new_tree[parent[i]].append(i)
        
        res = [0]*n
        def size(node):
            res[node]=1
            for child in new_tree[node]:
                res[node]+=size(child)
            return res[node]
        size(0)
        return res

        





















