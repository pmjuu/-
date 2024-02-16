def solution(n, k, cmd):
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]
    k += 1
    deleted = []
    
    for c in cmd:
        if c.startswith('C'):
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            deleted.append(k)
            k = up[k] if n < down[k] else down[k]
        elif c.startswith('Z'):
            restore = deleted.pop()
            up[down[restore]] = restore
            down[up[restore]] = restore
        else:
            action, num = c.split( ) 
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    answer = ["O"] * n
    
    for i in deleted:
        answer[i - 1] = "X"
        
    return "".join(answer)
