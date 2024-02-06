def solution(s):
    answer = 0
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
        
    return int(not stack)
