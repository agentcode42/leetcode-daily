class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k = dict(knowledge)
        res = []
        start = -1
        for i,c in enumerate(s):
            if c=="(":
                start = i
            if c==")":
                key = s[start+1:i]
                val = "?"
                if key in k:
                    val = k[key]
                res.append(val)
            elif start<0:
                res.append(c)
        return "".join(res)