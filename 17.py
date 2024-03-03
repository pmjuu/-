from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for char in goal:
        if cards1 and char == cards1[0]:
            cards1.popleft()
        elif cards2 and char == cards2[0]:
            cards2.popleft()
        else:
            return "No"
        
    return "Yes"
