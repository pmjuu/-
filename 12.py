def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    stack = [0]
    
    for i in range(1, n):
        
        while stack and prices[i] < prices[stack[-1]]: # i = 3
            j = stack.pop() # j = 2, stack = [0, 1]
            answer[j] = i - j # answer[2] = 1
            
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    
    return answer
