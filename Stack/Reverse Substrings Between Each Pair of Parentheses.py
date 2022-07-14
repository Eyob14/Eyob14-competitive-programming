class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                last_chain = stack.pop()
                stack[-1] += last_chain[::-1]
            else:
                stack[-1].append(c)
        
        return ''.join(stack[-1])