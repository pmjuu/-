from collections import defaultdict

def solution(participant, completion):
    hash = defaultdict(int)
    
    for p in participant:
        hash[p] += 1
    
    for c in completion:
        hash[c] -= 1
    
    for key in hash.keys():
        if hash[key] == 1:
            return key
