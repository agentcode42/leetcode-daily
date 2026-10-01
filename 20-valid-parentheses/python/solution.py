class Solution:
    def isValid(self, s: str) -> bool:
        table = {"(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if c in table:
                stack.append(c)
            else:
                if not stack or table[stack.pop()]!=c:
                    return False
        return not stack
                    