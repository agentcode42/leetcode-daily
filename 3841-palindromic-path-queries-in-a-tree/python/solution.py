class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        tree = defaultdict(list)
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)

        log = n.bit_length()
        parent = [[0]*n for _ in range(log)]
        tin,tout,depth = [0]*n,[0]*n,[0]*n
        timer = 0

        def dfs(u,p):
            nonlocal timer
            tin[u]=timer
            timer+=1
            parent[0][u]=p

            for v in tree[u]:
                if v!=p:
                    depth[v]=depth[u]+1
                    dfs(v,u)
            tout[u]=timer
        dfs(0,0)

        for k in range(1,log):
            for u in range(n):
                parent[k][u]=parent[k-1][parent[k-1][u]]
        
        fenwick = [0]*(n+2)

        def update_bit(i,mask):
            i+=1
            while i<len(fenwick):
                fenwick[i]^=mask
                i += i & -i
        def prefix_xor(i):
            mask = 0
            i+=1
            while i:
                mask^=fenwick[i]
                i -= i&-i
            return mask
        
        char_mask = [1 << (ord(c)-97) for c in s]

        for u in range(n):
            update_bit(tin[u],char_mask[u])
            update_bit(tout[u],char_mask[u])
        
        def lca(u,v):
            if depth[u]<depth[v]:
                u,v = v,u
            diff = depth[u]-depth[v]
            for k in range(log):
                if diff>>k&1:
                    u = parent[k][u]
            if u==v:
                return u
            for k in range(log -1,-1 ,-1):
                if parent[k][u]!=parent[k][v]:
                    u,v = parent[k][u],parent[k][v]
                
            return parent[0][u]
        
        answer = []

        for q in queries:
            parts = q.split()
            u = int(parts[1])

            if parts[0]=="update":
                new_mask = 1<<(ord(parts[2])-97)
                diff = char_mask[u] ^ new_mask
                update_bit(tin[u],diff)
                update_bit(tout[u],diff)
                char_mask[u]=new_mask
            else:
                v = int(parts[2])
                ancestor = lca(u,v)

                path_mask = (prefix_xor(tin[u]) 
                            ^ prefix_xor(tin[v]) 
                            ^char_mask[ancestor])
                answer.append((path_mask & (path_mask-1)) == 0)
        return answer













































































