from collections import defaultdict

def solution(want, number, discount):
    want_dict = defaultdict(int)
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    answer = 0
        
    for i in range(len(discount) - 9):
        discount_dict = defaultdict(int)
        
        for j in range(i, i + 10):
            discount_dict[discount[j]] += 1
    
        if (want_dict == discount_dict):
            answer += 1
        
    return answer
