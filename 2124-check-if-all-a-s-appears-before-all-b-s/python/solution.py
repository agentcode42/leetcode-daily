class Solution:
    def checkString(self, s: str) -> bool:
        flag_a = False
        flag_b = False
        for c in s:
            if c == "a":
                flag_a = True
                if flag_b:
                    return False
            else:
                flag_b = True
                
        return True