def is_valid_position(nx, ny):
    return -5 <= nx <= 5 and -5 <= ny <= 5

def update_position(x, y, dir):
    if dir == 'U':
        return x, y + 1
    elif dir == 'D':
        return x, y - 1
    elif dir == 'L':
        return x - 1, y
    elif dir == 'R':
        return x + 1, y

def solution(dirs):
    x, y = 0, 0
    answer = set()
    
    for dir in dirs:
        nx, ny = update_position(x, y, dir)
        
        if not is_valid_position(nx, ny):
            continue
        
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        
        x, y = nx, ny
    
    return len(answer) / 2
