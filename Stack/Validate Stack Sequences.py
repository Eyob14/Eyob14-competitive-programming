def validateStackSequences(pushed, popped):
    stack = []
    stack.append(pushed[0])
    pushed.pop(0)
    answer = False
    while len(popped) != 0:
        if len(stack) == 0 or stack[-1] != popped[0]:
            stack.append(pushed[0])
            pushed.pop(0)
        else:
            while stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        if stack[::-1] == popped:
            answer = True
    if len(popped) and len(stack):
        answer= False
    answer = True
    return answer
        
pushed = [2,1,0]
popped = [1,2,0]
print(validateStackSequences(pushed, popped))