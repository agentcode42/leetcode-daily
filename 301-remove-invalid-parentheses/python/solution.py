class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        min_remove = 0
        bal = 0
        for c in s:
            if c=="(":
                bal+=1
            elif c==")":
                bal-=1
                if bal<0:
                    min_remove+=1
                    bal+=1
        min_remove = min_remove+bal
        n = len(s)
        if min_remove == n:
            return [""]
        curr = []
        res = set()
        bal = 0
        def dfs(i,rem,bal):
            if i == n:
                if rem==min_remove and bal==0:
                    res.add("".join(curr))
                return 
            if bal<0:
                return 
            if rem>min_remove:
                return 
            curr.append(s[i])
            new_bal = bal
            if s[i]=="(":
                new_bal += 1
            elif s[i]==")":
                new_bal-=1
            dfs(i+1,rem,new_bal)
            curr.pop()
            if s[i] in "()":
                dfs(i+1,rem+1,bal)
            return 
        dfs(0,0,0)
        return list(res)