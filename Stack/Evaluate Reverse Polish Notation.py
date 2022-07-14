class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if t=="+":
                    stack.append(op1+op2)
                elif t=="-":
                    stack.append(op1-op2)
                elif t=="*":
                    stack.append(op1*op2)
                elif t=="/":
                    stack.append(int(op1/op2))
        return stack[-1]