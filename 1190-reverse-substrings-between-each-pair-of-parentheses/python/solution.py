class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c==')':
                curr = []
                while stack and stack[-1]!='(':
                    curr.append(stack.pop())
                stack.pop()
                stack.extend(curr)
            else:
                stack.append(c)
        return "".join(stack)