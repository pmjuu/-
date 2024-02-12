def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        i = move - 1

        for row in board:
            if (doll := row[i]) != 0:
                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                row[i] = 0
                break

    return answer

  
# walrus operator := https://docs.python.org/3/whatsnew/3.8.html
